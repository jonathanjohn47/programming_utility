# prompt: I need a script which works like this:
# I will provide a folder address and a new name for another folder which will be created nside this folder. Inside that new folder (whose name I've given), the script will create two more folders named "ui" and "get_controllers".
# So you have to accept two things from user. 1. Folder address and 2. Name.
# 'ui' and 'get_controllers' is fixed

import os


def create_folders():
    """Creates 'ui' and 'get_controllers' folders inside a new folder."""
    folder_address = input("Enter the folder address: ")
    new_folder_name = input("Enter the name for the new folder: ")

    new_folder_path = os.path.join(folder_address, new_folder_name)
    ui_folder_path = os.path.join(new_folder_path, "ui")
    get_controllers_folder_path = os.path.join(new_folder_path, "get_controllers")

    try:
        os.makedirs(new_folder_path)
        os.makedirs(ui_folder_path)
        os.makedirs(get_controllers_folder_path)
        print(f"Folders created successfully at {new_folder_path}")
    except FileExistsError:
        print(f"Folder already exists at {new_folder_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_folders()
