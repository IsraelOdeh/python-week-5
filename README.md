# File Handling in Python Program
This Python script demonstrates basic file handling operations: creating a new text file, writing content to it, reading the content, and appending additional lines. It uses error handling to manage potential file input/output errors.

## How It Works
- Define File Path:
The script sets a variable filename that specifies the path for the text file to be created or modified.
- Create and Write to the File:
The script attempts to create a new text file named my_file.txt in write mode ('w'). If successful, it writes at least three lines of text, including a mix of strings and numbers.
- Read the File Contents:
The script attempts to read the contents of my_file.txt and display them on the console. If it encounters an error while trying to open the file, it will print an error message.
- Append to the File:
The script opens my_file.txt in append mode ('a') and adds three additional lines of text to the existing content. It again handles any potential I/O errors.

## Requirements
Python 3.x installed on your system.
## How to Run
Download or copy the script to your local machine.
Open a terminal or command prompt and navigate to the directory where the script is saved.
Run the script by typing:

<code> python <script_name>.py </code>
 
## Notes
The script uses exception handling (try and except) to gracefully manage file I/O errors, such as issues with file creation or access.
Ensure that the script has permission to create and modify files in the specified directory.
