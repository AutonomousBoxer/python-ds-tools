python-ds-tools

## Installation

To install the `python-ds-tools` package, you can use pip:

```bash
pip install python-ds-tools
```

## Usage

### Color Picker Tool

The color picker tool allows you to select colors and copy their hex codes to the clipboard.

To use the color picker tool, run the following command:

```bash
python -m src.main.app
```

Then, click on the "Color Picker" button to open the color picker window. You can select a color by clicking on it, and the hex code of the selected color will be copied to the clipboard.

### Icon Creator Tool

The icon creator tool allows you to convert image files to ICO format.

To use the icon creator tool, run the following command:

```bash
python -m src.main.app
```

Then, click on the "Icon Creator" button to open the icon creator window. You can select an input file, generate a new file name, and select a save location. Click the "Convert" button to convert the selected file to ICO format.

### Excel Cleaner Tool

The excel cleaner tool allows you to clean Excel files by removing empty rows and columns.

To use the excel cleaner tool, run the following command:

```bash
python -m src.tools.excel_cleaner
```

The tool will process all Excel files in the specified directory, remove empty rows and columns, and save the cleaned files with "_cleaned" appended to the original file name.
