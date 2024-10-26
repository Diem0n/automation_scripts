# File Auto Organizer

## Description
The File Auto Organizer is a Python script that monitors a specified directory and automatically organizes files into subdirectories based on their file types (extensions). This tool helps simplify file management by grouping files together.

## Features
- Monitors a specified directory for new files.
- Creates subdirectories for each file type found.
- Moves files into their respective subdirectories.
- Prints the status of newly detected files in the console.

## Requirements
- Python 3.x
- `watchdog` library (install with `pip install watchdog`)

## Usage
1. **Clone the repository or download the script.**
2. **Open the script and modify the Downloads path:**
   - Change the line `downloads_path = Path("C:/Users/YourUsername/Downloads")` to point to your desired directory.
3. **Open a terminal or command prompt.**
4. **Navigate to the directory containing the script.**
5. **Run the script:**
   ```bash
   python script.py
