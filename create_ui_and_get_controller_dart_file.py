import os


def create_files(folder_path, name, initiateGetController: bool):
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
        ui_file.write(f'''import 'package:flutter/material.dart';
class {getCamelCase(name)}Screen extends StatelessWidget {{
  const {getCamelCase(name)}Screen({{super.key}});
  ''')

    with open(ui_file_path, 'a') as ui_file:
        if initiateGetController:
            ui_file.write(f'final controller = Get.put({getCamelCase(name)}GetController());\n')

    with open(ui_file_path, 'a') as ui_file:
        ui_file.write(f'''@override
          Widget build(BuildContext context) {{
            return Scaffold();
          }}
        }}''')

    # Create and open the 'update_request_get_controller.dart' file
    with open(controller_file_path, 'w') as controller_file:
        controller_file.write(
            f'''import 'package:get/get.dart';\nclass {getCamelCase(name)}GetController extends GetxController {{}}\n''')

    print(f"Files '{ui_file_name}' and '{controller_file_name}' were created successfully.")


def getCamelCase(name):
    words = name.split("_")
    camelCaseWords = []
    for word in words:
        camelCaseWords.append(word.capitalize())
    camelCaseName = ''.join(camelCaseWords)
    return camelCaseName


def main():
    folder_address = input("Enter the folder address: ").strip()
    name = input("Enter the name: ").strip()
    initiate_get_controller = input("Do you want to initiate GetxController? (y/n): ")
    create_files(folder_address, name, initiate_get_controller == 'y')


if __name__ == "__main__":
    main()
