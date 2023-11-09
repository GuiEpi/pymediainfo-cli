import typer
from pymediainfo import MediaInfo
from typing_extensions import Annotated
import json
from rich.table import Table
from rich.console import Console

app = typer.Typer()

console = Console()
err_console = Console(stderr=True, style="bold white on red")


class TrackValidationError(Exception):
    pass


def validate_tracks(media_info, general, video, audio, text, image, other, menu):
    track_types = {
        "General": general,
        "Video": video,
        "Audio": audio,
        "Text": text,
        "Image": image,
        "Other": other,
        "Menu": menu,
    }

    for track_type, flag in track_types.items():
        if flag and not any(
            track.track_type == track_type for track in media_info.tracks
        ):
            raise TrackValidationError(f"No {track_type.lower()} tracks found in file.")


def complete_output_format():
    return ["table", "json"]


@app.command()
def main(
    file_path: Annotated[
        str, typer.Argument(..., help="The path to the media file you want to analyze")
    ],
    output_format: Annotated[
        str,
        typer.Option(
            "--output-format",
            "-f",
            shell_complete=complete_output_format,
            help="Output format (table, json)",
        ),
    ] = "table",
    general: Annotated[
        bool, typer.Option("--general", "-g", help="Include General tracks")
    ] = False,
    video: Annotated[
        bool, typer.Option("--video", "-v", help="Include Video tracks")
    ] = False,
    audio: Annotated[
        bool, typer.Option("--audio", "-a", help="Include Audio tracks")
    ] = False,
    text: Annotated[
        bool, typer.Option("--text", "-t", help="Include Text tracks")
    ] = False,
    image: Annotated[
        bool, typer.Option("--image", "-i", help="Include Image tracks")
    ] = False,
    other: Annotated[
        bool, typer.Option("--other", "-o", help="Include Other tracks")
    ] = False,
    menu: Annotated[
        bool, typer.Option("--menu", "-m", help="Include Menu tracks")
    ] = False,
    parse_speed: Annotated[
        float, typer.Option("--parse-speed", "-p", help="MediaInfo parse speed (0-1)")
    ] = 0.5,
    output_file: Annotated[
        str, typer.Option(help="Write output to a file (optional)")
    ] = None,
):
    try:
        if not 0 <= parse_speed <= 1:
            raise ValueError("Parse speed must be between 0 and 1.")

        media_info = MediaInfo.parse(file_path, parse_speed=parse_speed)

        if any([general, video, audio, text, image, other, menu]):
            validate_tracks(media_info, general, video, audio, text, image, other, menu)

        if output_format == "json":
            output = json.dumps(media_info.to_data())
        else:
            output = ""
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Key")
            table.add_column("Value")
            for track in media_info.tracks:
                if (
                    (general and track.track_type == "General")
                    or (video and track.track_type == "Video")
                    or (audio and track.track_type == "Audio")
                    or (text and track.track_type == "Text")
                    or (image and track.track_type == "Image")
                    or (other and track.track_type == "Other")
                    or (menu and track.track_type == "Menu")
                    or (not any([general, video, audio, text, image, other, menu]))
                ):
                    track_data = track.to_data()
                    for key, value in track_data.items():
                        table.add_row(key, str(value))
            output = table

        if output_file and output_format != "json":
            console.print(output)
            raise ValueError("Output file can only be specified for JSON output.")

        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(output)
            typer.echo(f"Output written to {output_file}")
        else:
            if output_format == "json":
                console.print_json(output)
            else:
                console.print(output)

    except FileNotFoundError:
        err_console.print(f"Error: The file was not found. Please check the path.")
        raise typer.Exit(code=1)
    except ValueError as e:
        err_console.print(f"Error: {e}")
        raise typer.Exit(code=1)
    except TrackValidationError as e:
        err_console.print(f"Error: {e}")
        raise typer.Exit(code=1)
    except Exception as e:
        err_console.print(f"Error: {e}")
        raise typer.Exit(code=1)
