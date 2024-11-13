import os

import pyperclip


def create_get_controller(dart_file_path):
    # Extract the directory and file name from the given Dart file path
    directory = os.path.dirname(dart_file_path)
    dart_file_name = os.path.basename(dart_file_path)

    # Remove the extension from the Dart file name to get the base name
    base_name = os.path.splitext(dart_file_name)[0]

    # Create the get_controllers folder path
    get_controllers_folder_path = os.path.join(directory, 'get_controllers')

    # Ensure the get_controllers directory exists
    if not os.path.exists(get_controllers_folder_path):
        os.makedirs(get_controllers_folder_path)

    # Create the GetX controller file name
    controller_file_name = f"{base_name}_get_controller.dart"

    # Complete path for the new GetX controller file
    controller_file_path = os.path.join(get_controllers_folder_path, controller_file_name)

    # Create and open the GetX controller file
    with open(controller_file_path, 'w') as controller_file:
        controller_file.write(
            f'''import 'package:get/get.dart';\nclass {getCamelCase(base_name)}GetController extends GetxController {{}}\n''')

    print(f"GetX controller file '{controller_file_name}' created successfully at '{get_controllers_folder_path}'.")

    pyperclip.copy(f'{getCamelCase(base_name)}GetController getController = Get.put({getCamelCase(base_name)}GetController());')

def getCamelCase(name):
    words = name.split("_")
    camelCaseWords = []
    for word in words:
        camelCaseWords.append(word.capitalize())
    camelCaseName = ''.join(camelCaseWords)
    return camelCaseName

if __name__ == "__main__":
    dart_file_path = input("Enter the Dart file path: ").strip()
    create_get_controller(dart_file_path)