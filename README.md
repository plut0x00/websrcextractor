# Web Source Code Extractor

The Web Source Extractor is a Python script that helps you extract HTML, CSS, and JavaScript code from a web page. It utilizes the `requests` library to fetch the web page's source code and the `BeautifulSoup` library to parse and extract specific code sections.

## Features

- Get the source code of a web page by providing its URL.
- Extract and save HTML, CSS, and JavaScript code into separate files.
- Customize the output directory and filenames.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` library

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/plut0x00/websrcextractor.git
   ```

2. Install the required libraries:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```
   python websrcextractor.py
   ```

2. When prompted, enter the URL of the web page you want to extract code from.

3. Provide filenames for the output HTML, CSS, and JavaScript files.

4. The script will save the extracted code to the specified directory.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [Creative Commons Attribution License (CC BY)](LICENSE). You are free to use, modify, and distribute the code as long as you give appropriate credit to the original author.
