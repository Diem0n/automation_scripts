import os
import shutil
import sys
from pathlib import Path

def create_directories_for_file_types(addr):
    """Create directories for each file type in the specified address."""
    file_types = {file.suffix[1:] for file in addr.iterdir() if file.is_file()}
    for ext in file_types:
        dir_path = addr / ext
        dir_path.mkdir(exist_ok=True)

def move_files_to_directories(addr):
    """Move files to their respective directories based on file type and collect stats."""
    file_stats = {}

    for file in addr.iterdir():
        if file.is_file():
            ext = file.suffix[1:]  # Get file extension without dot
            dest_dir = addr / ext
            
            # Initialize stats for this file type if not already done
            if ext not in file_stats:
                file_stats[ext] = {'count': 0, 'total_size': 0}

            # Update stats
            file_stats[ext]['count'] += 1
            file_stats[ext]['total_size'] += file.stat().st_size
            
            try:
                shutil.move(str(file), str(dest_dir / file.name))
            except Exception as e:
                print(f"Error moving file {file.name}: {e}")

    return file_stats


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path1> <directory_path2> ...")
        sys.exit(1)

    for arg in sys.argv[1:]:
        addr = Path(arg)

        if not addr.is_dir():
            print(f"The directory '{addr}' does not exist.")
            continue

        create_directories_for_file_types(addr)
        file_stats = move_files_to_directories(addr)


if __name__ == "__main__":
    main()
