# PyMediaInfo CLI

![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Test](https://github.com/GuiEpi/pymediainfo-cli/actions/workflows/python-ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/GuiEpi/pymediainfo-cli/graph/badge.svg?token=9EK12X8FX9)](https://codecov.io/gh/GuiEpi/pymediainfo-cli)

This is a command-line interface (CLI) for the PyMediaInfo library, which provides a way to extract metadata from media files.

## Installation

You can install this CLI using pip:

```bash
pip install pymediainfo-cli
```
## Usage
You can use this CLI by running the pymediainfo command followed by the path to a media file:
```bash
pymediainfo path/to/media/fil
```

This will print the metadata for the media file in a human-readable format.

You can also specify various options to control the output. For example, you can use the --json option to output the metadata in JSON format:
```bash
pymediainfo --json path/to/media/file
```

## Testing
You can run the unit tests for this CLI using the unittest module:
```bash
python3 run pytest tests/test.py
```

Replace test with the name of your test file.


## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## License
This project is licensed under the MIT License.