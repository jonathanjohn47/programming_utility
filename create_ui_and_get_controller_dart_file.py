import os


def create_files(folder_path, name):
    # Paths for the 'ui' and 'get_controllers' directories
    ui_folder_path = os.path.join(folder_path, 'ui')
    get_controllers_folder_path = os.path.join(folder_path, 'get_controllers')

    # Ensure that the 'ui' and 'get_controllers' directories exist
    if not os.path.exists(ui_folder_path):
        os.makedirs(ui_folder_path)
    if not os.path.exists(get_controllers_folder_path):
        os.makedirs(get_controllers_folder_path)

    # Deducing file names from the given name
    ui_file_name = f"{name}_screen.dart"
    controller_file_name = f"{name}_get_controller.dart"

    # Complete paths for the new files
    ui_file_path = os.path.join(ui_folder_path, ui_file_name)
    controller_file_path = os.path.join(get_controllers_folder_path, controller_file_name)

    # Create and open the 'update_request_screen.dart' file
    with open(ui_file_path, 'w') as ui_file:
        ui_file.write('// Dart code for UI screen goes here\n')

    # Create and open the 'update_request_get_controller.dart' file
    with open(controller_file_path, 'w') as controller_file:
        controller_file.write('// Dart code for GetX controller goes here\n')

    print(f"Files '{ui_file_name}' and '{controller_file_name}' were created successfully.")


def main():
    folder_address = input("Enter the folder address: ").strip()
    name = input("Enter the name: ").strip()
    create_files(folder_address, name)


if __name__ == "__main__":
    main()
