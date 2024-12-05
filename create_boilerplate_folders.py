import os
folders_to_create = ['features', 'utility', 'core', 'models']
def create_boilerplate_folders(folder_path):
    for folder in folders_to_create:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
        print(f"Created folder: {os.path.join(folder_path, folder)}")


if __name__ == "__main__":
    folder_address = input("Enter the folder address: ").strip()
    create_boilerplate_folders(folder_address)