from pathlib import Path

from categories import CATEGORIES, get_category


def get_unique_path(destination):
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_folder(folder_path):
    root = Path(folder_path).expanduser().resolve()

    if not root.exists():
        raise FileNotFoundError(f"Folder not found: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Not a folder: {root}")

    summary = {category: 0 for category in CATEGORIES}
    summary["misc"] = 0
    total_files = 0

    for item in root.iterdir():
        if not item.is_file():
            continue

        category = get_category(item)
        category_folder = root / category
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / item.name
        destination = get_unique_path(destination)

        item.rename(destination)
        summary[category] += 1
        total_files += 1

    return summary, total_files