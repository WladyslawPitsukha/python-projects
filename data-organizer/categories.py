CATEGORIES = {
    "images": {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"},
    "videos": {".mp4", ".mov", ".avi", ".mkv", ".wmv"},
    "audio": {".mp3", ".wav", ".flac", ".aac"},
    "documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".csv", ".xlsx", ".xls"},
    "code": {".py", ".js", ".ts", ".html", ".css", ".json", ".md"},
    "archives": {".zip", ".rar", ".tar", ".gz", ".7z"},
    "executables": {".exe", ".msi", ".dmg"},
}


def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "misc"