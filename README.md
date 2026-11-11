# Automated File Organizer & Cleanup Utility

## Introduction

The Automated File Organizer & Cleanup Utility is a Python-based desktop automation project designed to organize cluttered directories such as Downloads and Desktop.

It automatically identifies files according to their extensions and moves them into appropriate category folders.

The project reduces manual file management and improves directory organization.

## Objectives

1. Automate file organization.
2. Identify file types using extensions.
3. Create category folders dynamically.
4. Move files using Python filesystem operations.
5. Handle filename collisions.
6. Handle permission exceptions.
7. Generate an execution summary.

## Technologies Used

Technology| Purpose

Python 3| Programming language

OS| Directory scanning

shutil| Moving files

pathlib| File and directory paths

No external libraries are required.

## Project Structure

Automated-File-Organizer/

├── organizer.py

└── README.md

## File Categories

Category| Extensions

Documents| PDF, DOCX, TXT, XLSX, PPTX

Images| JPG, JPEG, PNG, GIF, SVG

Videos| MP4, MKV, AVI, MOV

Archives| ZIP, RAR, 7Z, TAR

Code| PY, JAVA, C, CPP, HTML, CSS, JS

Others| Unrecognized extensions

## Working Methodology

1. Specify the target directory.
2. Scan directory entries using "os.scandir()".
3. Identify regular files.
4. Extract file extensions using "pathlib".
5. Match extensions using the mapping dictionary.
6. Create category folders using "mkdir()".
7. Check destination filenames to avoid collisions.
8. Move files using "shutil.move()".
9. Handle permission and filesystem exceptions.
10. Display the final execution summary.

## How to Execute

Step 1: Install Python 3.

Step 2: Create "organizer.py".

Step 3: Configure the target directory.

Example:

TARGET_DIR = Path.home() / "Downloads"

Step 4: Open the terminal in the project directory.

Step 5: Execute:
```
python organizer.py
```
Step 6: Type YES to start organizing.

## Sample Output
```
AUTOMATED FILE ORGANIZER
--------------------------------------------------
Target Directory: Downloads

Type YES to organize files: YES

Starting File Organizer
--------------------------------------------------
[MOVED] notes.pdf -> Documents
[MOVED] photo.jpg -> Images
[MOVED] video.mp4 -> Videos
[MOVED] project.zip -> Archives
[MOVED] program.py -> Code

==================================================
       FILE ORGANIZER SUMMARY
==================================================
Total Files Scanned : 5
Files Relocated     : 5
Files Skipped       : 0
Errors              : 0
==================================================
Organization Completed!

Note: This is illustrative output.
```
## Exception Handling

- "PermissionError": Handles files that cannot be accessed because of permissions.
- "OSError": Handles filesystem-related errors.
- Filename collision: Generates a unique filename using numeric suffixes.

## Advantages

1. Saves time.
2. Reduces manual effort.
3. Improves file management.
4. Prevents intentional overwriting of existing files.
5. Supports multiple file categories.
6. Uses Python built-in modules.

## Limitations

1. Processes files directly inside the selected directory, not recursively.
2. Requires appropriate directory permissions.
3. Classification depends on file extensions.
4. Unknown extensions are placed in Others.

## Future Enhancements

1. Graphical User Interface using Tkinter.
2. Automatic scheduled organization.
3. Duplicate file detection.
4. File size-based categorization.
5. Detailed log file generation.
6. Recursive directory organization.
