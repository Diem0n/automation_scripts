import os
import shutil
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class FileHandler(FileSystemEventHandler):
    def __init__(self, monitored_dir):
        self.monitored_dir = Path(monitored_dir)

    def on_created(self, event):
        # Trigger only for files, not directories
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            self.organize_files()

    def organize_files(self):
        """Organize files in the monitored directory."""
        file_stats = {}
        for file in self.monitored_dir.iterdir():
            if file.is_file():
                ext = file.suffix[1:]
                dest_dir = self.monitored_dir / ext
                if ext not in file_stats:
                    file_stats[ext] = {'count': 0, 'total_size': 0}

                file_stats[ext]['count'] += 1
                file_stats[ext]['total_size'] += file.stat().st_size

                try:
                    shutil.move(str(file), str(dest_dir / file.name))
                except Exception as e:
                    print(f"Error moving file {file.name}: {e}")


def main():
    downloads_path = Path("C:/Users/YourUsername/Downloads")
    if not downloads_path.is_dir():
        print(f"The directory '{downloads_path}' does not exist.")
        sys.exit(1)

    event_handler = FileHandler(downloads_path)
    observer = Observer()
    observer.schedule(event_handler, downloads_path, recursive=False)
    observer.start()

    print(f"Monitoring directory: {downloads_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
