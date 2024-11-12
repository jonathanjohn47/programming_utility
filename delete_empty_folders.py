import os

def delete_empty_folders(folder_path):
    """Deletes all empty folders inside the given folder."""
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # Check if the directory is empty
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")

if __name__ == "__main__":
    folder_address = input("Enter the folder address: ").strip()
    delete_empty_folders(folder_address)