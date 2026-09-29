import os

from organizer import organize_folder
from reporter import print_report


def main():
    print("=== Data Organizer ===")
    print("Sort files into folders by file type.\n")

    folder = input(
        "Enter a folder path, or press Enter for the current folder: "
    ).strip()

    folder_path = folder or os.getcwd()

    try:
        summary, total_files = organize_folder(folder_path)
        print_report(summary, total_files)
        print("\nOrganization complete.")

    except FileNotFoundError as error:
        print(f"\nError: {error}")

    except NotADirectoryError as error:
        print(f"\nError: {error}")

    except PermissionError:
        print("\nError: Permission denied. Try another folder.")

    except OSError as error:
        print(f"\nFile system error: {error}")


if __name__ == "__main__":
    main()