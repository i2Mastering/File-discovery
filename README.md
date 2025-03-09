# Path Converter

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Example](#example)
7. [License](#license)

## Overview
This Python script, **Path Converter**, converts a file path to match the file path format conventions of your operating system. It ensures cross-platform compatibility by adapting path separators to the current OS environment.

This project was developed by **Ike Iloegbu** as part of **CSC 6303 Project 6**, tested on **macOS 15.0.1**.

## Features
- Automatically detects your operating system.
- Converts file paths:
  - Converts to forward slashes (`/`) on macOS.
  - Converts to backslashes (`\`) on Windows.
- Cleans and normalizes file paths for consistency.

## Requirements
- Python 3.x
- Works on macOS, Windows, and Linux (with macOS and Windows-specific path handling)

## Installation
No additional packages are required. This script uses Python's built-in `os` and `platform` modules.

1. Clone or download the script.
2. Ensure Python 3 is installed on your machine.

## Usage
1. Run the script using Python:
   ```bash
   python3 path_converter.py
   ```
2. Follow the prompt to enter a file path. Example:
   ```
   Please enter the file name with the path: C:\\Users\\Example\\Documents\\file.txt
   ```
3. The script will output the converted path based on your OS.

## Example
### On macOS
```
Computer operating system: Darwin
Please enter the file name with the path: C:\\Users\\Example\\Documents\\file.txt
Converted Path: C:/Users/Example/Documents/file.txt
```

### On Windows
```
Computer operating system: Windows
Please enter the file name with the path: /Users/Example/Documents/file.txt
Converted Path: \Users\Example\Documents\file.txt
```

## License
This project is provided for educational purposes.

---

'''  
Ike Iloegbu CSC 6303 Project 6  
Tested on macOS 15.0.1  
'''

import platform
import os

def path(file_path):
    '''
    Converts a given file path to the appropriate format based on the user's operating system.

    This function performs the following steps:
    1. Detects the current operating system.
    2. Normalizes the input path to eliminate redundant separators and up-level references.
    3. Converts path separators based on OS:
       - For macOS (Darwin), ensures the use of forward slashes ('/').
       - For other operating systems (e.g., Windows), converts to backslashes ('\\').

    Args:
        file_path (str): The original file path entered by the user.

    Returns:
        str: The converted file path compatible with the user's OS.
    '''

    current_os = platform.system()
    normpath = os.path.normpath(file_path)

    if current_os == "Darwin":
        converted_path = normpath.replace("\\", "/")
    else:
        converted_path = normpath.replace("/", "\\")

    return converted_path

def main():
    '''
    Main function to interact with the user, accept a file path, and display the converted path.

    This function performs the following steps:
    1. Detects and displays the user's current operating system.
    2. Prompts the user to enter a file path.
    3. Converts the entered path based on the OS.
    4. Displays the converted file path.
    '''

    current_os = platform.system()
    print(f"Computer operating system: {current_os}")

    filepath = input("Please enter the file name with the path: ")
    convertpath = path(filepath)

    print(f"Converted Path: {convertpath}")

if __name__ == "__main__":
    main()
