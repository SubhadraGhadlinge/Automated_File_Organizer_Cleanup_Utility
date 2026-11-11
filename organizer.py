import os
import shutil
import logging
from pathlib import Path
import argparse

# File extension mapping
EXTENSION_MAP = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    ".pptx": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",

    # Code
    ".py": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
    ".sql": "Code"
}


def get_unique_path(destination):

    if not destination.exists():
        return destination

    name = destination.stem
    extension = destination.suffix
    folder = destination.parent

    counter = 1

    while True:
        new_path = folder / f"{name}_{counter}{extension}"

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(directory, dry_run=True):

    source = Path(directory)

    if not source.exists() or not source.is_dir():
        print("Invalid directory!")
        return

    stats = {
        "moved": 0,
        "preview": 0,
        "errors": 0,
        "skipped": 0
    }

    logging.basicConfig(
        filename=source / "organizer.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    print("\nStarting File Organizer...")
    print("Directory:", source)

    try:
        with os.scandir(source) as entries:

            for entry in entries:

                try:
                    if entry.name == "organizer.log":
                        continue

                    if entry.is_symlink() or not entry.is_file(
                        follow_symlinks=False
                    ):
                        stats["skipped"] += 1
                        continue

                    file_path = Path(entry.path)

                    extension = file_path.suffix.lower()

                    category = EXTENSION_MAP.get(
                        extension, "Others"
                    )

                    destination_folder = source / category

                    destination = get_unique_path(
                        destination_folder / file_path.name
                    )

                    if dry_run:
                        print(
                            f"[PREVIEW] {file_path.name} "
                            f"-> {category}/"
                        )
                        stats["preview"] += 1

                    else:
                        destination_folder.mkdir(
                            parents=True,
                            exist_ok=True
                        )

                        destination = get_unique_path(
                            destination_folder / file_path.name
                        )

                        shutil.move(
                            str(file_path),
                            str(destination)
                        )

                        print(
                            f"[MOVED] {file_path.name} "
                            f"-> {category}/"
                        )

                        logging.info(
                            "Moved %s to %s",
                            file_path.name,
                            destination
                        )

                        stats["moved"] += 1

                except PermissionError as error:
                    print("Permission denied:", error)
                    logging.error(str(error))
                    stats["errors"] += 1

                except OSError as error:
                    print("File operation error:", error)
                    logging.error(str(error))
                    stats["errors"] += 1

    except PermissionError as error:
        print("Cannot access directory:", error)
        return

    except OSError as error:
        print("Directory error:", error)
        return

    print("\n========== EXECUTION SUMMARY ==========")

    print("Files moved:", stats["moved"])
    print("Files in preview:", stats["preview"])
    print("Skipped entries:", stats["skipped"])
    print("Errors:", stats["errors"])

    print("=======================================")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Automated File Organizer"
    )

    parser.add_argument(
        "directory",
        nargs="?",
        default=str(Path.home() / "Downloads"),
        help="Directory to organize"
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files"
    )

    args = parser.parse_args()

    organize_files(
        args.directory,
        dry_run=not args.apply
    )