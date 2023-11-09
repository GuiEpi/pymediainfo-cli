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

        result = runner.invoke(
            app, ["test.mp4", "--output-format", "json", "--general"]
        )
        assert result.exit_code == 0
        assert '"key": "value"' in result.stdout


def test_main_table_output():
    with patch("pymediainfo.MediaInfo.parse") as mock_parse:
        mock_track = MagicMock()
        mock_track.to_data.return_value = {"key": "value"}
        mock_track.track_type = "General"

        mock_media_info = MagicMock()
        mock_media_info.to_data.return_value = [mock_track.to_data()]
        mock_media_info.tracks = [mock_track]
        mock_parse.return_value = mock_media_info

        result = runner.invoke(app, ["test.mp4", "--general"])
        assert result.exit_code == 0
        assert "Key" in result.stdout
        assert "Value" in result.stdout


def test_main_file_not_found():
    result = runner.invoke(app, ["nonexistent.mp4"])
    assert result.exit_code == 1
    assert "Error: The file was not found. Please check the path." in result.stdout


def test_main_validation_error():
    with patch("pymediainfo.MediaInfo.parse") as mock_parse:
        mock_parse.side_effect = Exception("Custom error message")
        result = runner.invoke(app, ["test.mp4"])
        assert result.exit_code == 1
        assert "Error: Custom error message" in result.stdout
