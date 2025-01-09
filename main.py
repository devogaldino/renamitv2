import os
import unicodedata
import re

def slugify(text):
    """
    Converts text to a URL-friendly slug format.
    """
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[\s_-]+', '-', text)

def rename_files_folder(file_path):
    """
    Renames all files in the folder by applying a slug to their names.

    Args:
        file_path (str): Path of the folder containing the files.
    """
    if not os.path.isdir(file_path):
        print(f"Error: {file_path} is not a valid folder.")
        return

    for file_name in os.listdir(file_path):
        complete_path = os.path.join(file_path, file_name)

        if os.path.isfile(complete_path):
            name, ext = os.path.splitext(file_name)
            name_slug = slugify(name)
            new_name = f"{name_slug}{ext}"
            new_path = os.path.join(file_path, new_name)

            try:
                os.rename(complete_path, new_path)
                print(f"Renamed: {file_name} -> {new_name}")
            except Exception as e:
                print(f"Error to rename {file_name}: {e}")

# Exemplo de uso
enter_path = input("Enter the folder path: ")
rename_files_folder(enter_path)
