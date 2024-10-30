import os

import pyperclip
def rename_file(new_name):
    # Hardcoded file path
    file_path = '/Users/jonathanjohn/StudioProjects/sme_user/assets/images/img.png'

    # Ensure the new name has a .png extension
    if not new_name.endswith('.png'):
        new_name += '.png'

    # Directory of the file
    directory = os.path.dirname(file_path)

    # New file path
    new_file_path = os.path.join(directory, new_name)

    try:
        # Rename the file
        os.rename(file_path, new_file_path)
        print(f'Renamed: img.png -> {new_name}')
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    new_name = input("Enter the new name for the file (without extension): ").strip()
    rename_file(new_name)
