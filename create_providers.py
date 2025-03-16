import os

def create_folders():
    """Creates 'ui' and 'providers' folders inside a new folder."""
    folder_address = input("Enter the folder address: ")
    new_folder_name = input("Enter the name for the new folder: ")

    new_folder_path = os.path.join(folder_address, new_folder_name)
    ui_folder_path = os.path.join(new_folder_path, "ui")
    providers_folder_path = os.path.join(new_folder_path, "providers")

    try:
        os.makedirs(new_folder_path)
        os.makedirs(ui_folder_path)
        os.makedirs(providers_folder_path)
        print(f"Folders created successfully at {new_folder_path}")
    except FileExistsError:
        print(f"Folder already exists at {new_folder_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_folders()