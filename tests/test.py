from typer.testing import CliRunner
from unittest.mock import patch, MagicMock
from pymediainfo_cli.main import app

runner = CliRunner()


def test_main_json_output():
    with patch("pymediainfo.MediaInfo.parse") as mock_parse:
        mock_track = MagicMock()
        mock_track.to_data.return_value = {"key": "value"}
        mock_track.track_type = "General"
        mock_media_info = MagicMock()
        mock_media_info.to_data.return_value = [mock_track.to_data()]
        mock_media_info.tracks = [mock_track]
        mock_parse.return_value = mock_media_info

        file_path = "test.mp4"
        parse_speed = 0.5
        result = runner.invoke(app, [file_path, "--output-format", "json", "--general"])

        assert result.exit_code == 0
        assert '"key": "value"' in result.stdout
        mock_parse.assert_called_with(file_path, parse_speed=parse_speed)


def test_main_table_output():
    with patch("pymediainfo.MediaInfo.parse") as mock_parse:
        mock_track = MagicMock()
        mock_track.to_data.return_value = {"key": "value"}
        mock_track.track_type = "General"

        mock_media_info = MagicMock()
        mock_media_info.to_data.return_value = [mock_track.to_data()]
        mock_media_info.tracks = [mock_track]
        mock_parse.return_value = mock_media_info

        file_path = "test.mp4"
        parse_speed = 0.5
        result = runner.invoke(
            app, [file_path, "--output-format", "table", "--general"]
        )
        assert result.exit_code == 0
        assert "Key", "Value" in result.stdout
        mock_parse.assert_called_with(file_path, parse_speed=parse_speed)


def test_main_output_with_custom_parse_speed():
    with patch("pymediainfo.MediaInfo.parse") as mock_parse:
        mock_track = MagicMock()
        mock_track.to_data.return_value = {"key": "value"}
        mock_track.track_type = "General"
        mock_media_info = MagicMock()
        mock_media_info.to_data.return_value = [mock_track.to_data()]
        mock_media_info.tracks = [mock_track]
        mock_parse.return_value = mock_media_info

        file_path = "test.mp4"
        custom_parse_speed = 0.8
        result = runner.invoke(
            app, [file_path, "--parse-speed", str(custom_parse_speed)]
        )

        assert result.exit_code == 0
        assert "Key", "Value" in result.stdout
        mock_parse.assert_called_with(file_path, parse_speed=custom_parse_speed)


def test_main_file_not_found():
    result = runner.invoke(app, ["nonexistent.mp4"])
    assert result.exit_code == 1
    assert "Error: The file was not found. Please check the path." in result.stdout


def test_main_output_file_with_non_json_format():
    with patch("pymediainfo.MediaInfo.parse") as mock_parse:
        mock_parse.return_value = MagicMock()
        result = runner.invoke(
            app, ["test.mp4", "--output-format", "table", "--output-file", "output.txt"]
        )
        assert result.exit_code == 1
        assert "Output file can only be specified for JSON output." in result.stdout


def test_main_validation_error():
    with patch("pymediainfo.MediaInfo.parse") as mock_parse:
        mock_track = MagicMock()
        mock_track.track_type = "Video"
        mock_media_info = MagicMock()
        mock_media_info.tracks = [mock_track]
        mock_parse.return_value = mock_media_info

        result = runner.invoke(app, ["test.mp4", "--audio"])
        assert result.exit_code == 1
        assert "Error: No audio tracks found in file." in result.stdout


def test_main_general_exception():
    with patch("pymediainfo.MediaInfo.parse") as mock_parse:
        mock_parse.side_effect = Exception("Unexpected error")

        result = runner.invoke(app, ["test.mp4"])
        assert result.exit_code == 1
        assert "Error: Unexpected error" in result.stdout


def test_main_invalid_parse_speed():
    result = runner.invoke(app, ["test.mp4", "--parse-speed", "1.5"])  # Valeur invalide
    assert result.exit_code == 1
    assert "Parse speed must be between 0 and 1." in result.stdout
