import os
import pyperclip
import shutil


def create_get_controller(dart_file_path):
    # Extract the file name and base name from the Dart file path
    dart_file_name = os.path.basename(dart_file_path)
    base_name = os.path.splitext(dart_file_name)[0]

    # Extract the name of the parent folder from the Dart file's name
    parent_folder = base_name.split("_screen")[0] if "_screen" in base_name else base_name

    # Extract the directory and ensure parent_folder exists within the same directory
    dart_file_directory = os.path.dirname(os.path.abspath(dart_file_path)).strip()
    parent_folder_path = os.path.join(dart_file_directory, parent_folder)

    if not os.path.exists(parent_folder_path):
        os.makedirs(parent_folder_path, exist_ok=True)

    # Paths for "ui" and "get_controllers" folders
    ui_folder_path = os.path.join(parent_folder_path, 'ui')
    get_controllers_folder_path = os.path.join(parent_folder_path, 'get_controllers')

    # Ensure these directories exist
    os.makedirs(ui_folder_path, exist_ok=True)
    os.makedirs(get_controllers_folder_path, exist_ok=True)

    # Move Dart file to "ui" directory
    ui_dart_file_path = os.path.join(ui_folder_path, dart_file_name)
    shutil.move(dart_file_path, ui_dart_file_path)

    # Modify the UI Dart file
    modify_ui_dart_file(ui_dart_file_path, base_name, get_controllers_folder_path)

    # Create the GetX controller file name
    controller_file_name = f"{base_name}_get_controller.dart"

    # Complete path for the new GetX controller file
    controller_file_path = os.path.join(get_controllers_folder_path, controller_file_name)

    # Create and open the GetX controller file
    with open(controller_file_path, 'w') as controller_file:
        controller_file.write(
            f'''import 'package:get/get.dart';\n\nclass {getCamelCase(base_name)}GetController extends GetxController {{}}\n''')

    print(f"GetX controller file '{controller_file_name}' created successfully at '{get_controllers_folder_path}'.")

    pyperclip.copy(
        f'{getCamelCase(base_name)}GetController getController = Get.put({getCamelCase(base_name)}GetController());')


def modify_ui_dart_file(ui_dart_file_path, base_name, get_controllers_folder_path):
    # Read the content of the Dart file
    with open(ui_dart_file_path, 'r') as file:
        lines = file.readlines()

    # Prepare the import and controller lines
    import_line_get = "import 'package:get/get.dart';\n"
    import_line_controller = f"import '../get_controllers/{base_name}_get_controller.dart';\n"
    controller_init_line = f'  final {getCamelCase(base_name)}GetController getController = Get.put({getCamelCase(base_name)}GetController());\n'

    # Insert GetX import and initiate controller
    with open(ui_dart_file_path, 'w') as file:
        imported_get = False
        imported_controller = False
        controller_initiated = False
        for line in lines:
            if "import" in line and not imported_get:
                file.write(import_line_get)
                imported_get = True
            if import_line_get in line:
                file.write(line)
            if not imported_controller and line.startswith("import"):
                file.write(import_line_controller)
                imported_controller = True
            if "extends State<" in line and not controller_initiated:
                file.write(line)
                file.write(controller_init_line)
                controller_initiated = True
            else:
                file.write(line)


def getCamelCase(name):
    words = name.split("_")
    camelCaseWords = []
    for word in words:
        camelCaseWords.append(word.capitalize())
    camelCaseName = ''.join(camelCaseWords)
    return camelCaseName


if __name__ == "__main__":
    file_paths = [
        "/Users/jonathanjohn/StudioProjects/providers_practice/lib/other_screen.dart"

        ]
    for dart_file_path in file_paths:
        create_get_controller(dart_file_path)
