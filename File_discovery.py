'''
Author: Ike Iloegbu
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
