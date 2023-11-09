# PyMediaInfo CLI

![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
[![PyPI version](https://badge.fury.io/py/pymediainfo-cli.svg)](https://badge.fury.io/py/pymediainfo-cli)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Test](https://github.com/GuiEpi/pymediainfo-cli/actions/workflows/python-ci.yml/badge.svg)
[![Codecov](https://codecov.io/gh/GuiEpi/pymediainfo-cli/graph/badge.svg?token=9EK12X8FX9)](https://codecov.io/gh/GuiEpi/pymediainfo-cli)

This is a command-line interface (CLI) for the [pymediainfo](https://pypi.org/project/pymediainfo/) library, which provides a way to extract metadata from media files.

## [Requirement](https://pymediainfo.readthedocs.io/en/stable/index.html#requirements)
pymediainfo is a simple wrapper around the MediaInfo library, which you can find at https://mediaarea.net/en/MediaInfo.
> * Without the library, this package cannot parse media files, which severely limits its functionality.
> * Binary wheels containing a bundled library version are provided for Windows and Mac OS X.
> * Packages are available for [several major Linux distributions](https://repology.org/project/python:pymediainfo/versions). They depend on the library most of the time and are the preferred way to use pymediainfo on Linux unless a specific version of the package is required.

## Installation
You can install this CLI using pip:

```bash
pip install pymediainfo-cli
```

## Usage
You can use this CLI by running the pymediainfo command followed by the path to a media file:
```bash
pymediainfo-cli path/to/media/file
```
This will print the metadata for the media file in a human-readable format.

You can also specify various options to control the output:
* `--output-format` or `-f`: Output format (table, json)
* `--general` or `-g`: Include General tracks
* `--video` or `-v`: Include Video tracks
* `--audio` or `-a`: Include Audio tracks
* `--text` or `-t`: Include Text tracks
* `--image` or `-i`: Include Image tracks
* `--other` or `-o`: Include Other tracks
* `--menu` or `-m`: Include Menu tracks
* `--parse-speed` or `-p`: MediaInfo parse speed (0-1)
* `--output-file`: Write output to a file (optional)

For example, you can use the `-f json` to output the metadata in JSON format:
```bash
pymediainfo-cli path/to/media/file -f json
```

More information with:
```bash
pymediainfo-cli --help
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request.
> I use Poetry to mange dependancies see: https://python-poetry.org/

#### Clone the repo
```bash
git clone https://github.com/GuiEpi/pymediainfo-cli.git
```
#### Install dependancies 
```bash
poetry install
```
#### Run
```bash
poetry run pymediainfo-cli --help
```
#### Testing
```bash
poetry run pytest tests/test.py
```

## License
This project is licensed under the MIT License.

## Credits
This project was inspired by [pymediainfo](https://pypi.org/project/pymediainfo/).