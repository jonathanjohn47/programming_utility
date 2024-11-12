import os
import shutil


def delete_empty_folders(folder_path):
    """Deletes all empty folders inside the given folder."""
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # Check if the directory is empty
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")

def delete_non_git_folders(folder_path):
    for dir_name in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir_name)
        if os.path.isdir(dir_path):
            git_folder_path = os.path.join(dir_path, '.git')
            if not os.path.exists(git_folder_path):
                shutil.rmtree(dir_path)
                print(f"Deleted non-git folder: {dir_path}")
if __name__ == "__main__":
    folder_address = input("Enter the folder address: ").strip()
    delete_non_git_folders(folder_address)