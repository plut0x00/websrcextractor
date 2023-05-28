"""
Web Source Code Extractor
Author: plut0x00
Date: May 28, 2023
"""

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import html.parser
import os

def get_source_code(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Send a GET request to the specified URL
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Raise exception for non-2xx status codes

        # Detect and set the correct encoding
        encoding = response.encoding if response.encoding else 'utf-8'
        response.encoding = encoding

        return response.text
    except RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
url = input("Enter the URL: ")
source_code = get_source_code(url)

if source_code:
    soup = BeautifulSoup(source_code, 'html.parser')
    formatted_code = html.parser.unescape(soup.prettify())

    # Create directory to save the files
    output_dir = "/"
    os.makedirs(output_dir, exist_ok=True)

    # Save HTML code to a file
    html_filename = input("Enter the HTML filename to save the output to: ")
    html_file_path = os.path.join(output_dir, html_filename + ".html")
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_code)
    print(f"The HTML output has been saved to {html_file_path}.")

    # Save CSS code to a file
    css_code = ""
    for style_tag in soup.find_all('style'):
        css_code += style_tag.string + "\n"
    css_filename = input("Enter the CSS filename to save the output to: ")
    css_file_path = os.path.join(output_dir, css_filename + ".css")
    with open(css_file_path, 'w', encoding='utf-8') as file:
        file.write(css_code)
    print(f"The CSS output has been saved to {css_file_path}.")

    # Save JavaScript code to a file
    js_code = ""
    for script_tag in soup.find_all('script'):
        if script_tag.string:
            js_code += script_tag.string + "\n"
    js_filename = input("Enter the JavaScript filename to save the output to: ")
    js_file_path = os.path.join(output_dir, js_filename + ".js")
    with open(js_file_path, 'w', encoding='utf-8') as file:
        file.write(js_code)
    print(f"The JavaScript output has been saved to {js_file_path}.")
