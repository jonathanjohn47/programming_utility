import os
import re

folders_to_create = ['features', 'utility', 'components', 'models']
imports_to_add = [
    "import 'package:flutter_screenutil/flutter_screenutil.dart';",
    "import 'package:get/get.dart';"
]


def create_boilerplate_folders(folder_path):
    for folder in folders_to_create:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
        print(f"Created folder: {os.path.join(folder_path, folder)}")


def modify_main_dart(lib_path):
    main_dart_path = os.path.join(lib_path, 'main.dart')

    if not os.path.exists(main_dart_path):
        print(f"Warning: main.dart not found at {main_dart_path}. Skipping modification.")
        return

    try:
        with open(main_dart_path, 'r') as file:
            content = file.read()

        # Add missing imports
        for import_statement in imports_to_add:
            if import_statement not in content:
                content = import_statement + '\n' + content

        # Replace MaterialApp with GetMaterialApp
        content = content.replace('MaterialApp(', 'GetMaterialApp(')

        # Wrap GetMaterialApp with ScreenUtilInit if not already wrapped
        if "ScreenUtilInit(" not in content:
            start_index = content.find("GetMaterialApp(")
            if start_index != -1:
                open_bracket_count = 1
                index = start_index + len("GetMaterialApp(")
                while index < len(content):
                    if content[index] == '(':
                        open_bracket_count += 1
                    elif content[index] == ')':
                        open_bracket_count -= 1

                    if open_bracket_count == 0:
                        break
                    index += 1

                if index < len(content):

                    modified_content = content[
                                       :start_index] + 'ScreenUtilInit(\n        builder: (context, child) {\n                return ' + content[
                                                                                                                                         start_index:index + 1] + '\n          },\n        );' + content[
                                                                                                                                                                                                index + 1:]
                    content = modified_content
                else:
                    print("Could not wrap GetMaterialApp with ScreenUtilInit, something went wrong")

        with open(main_dart_path, 'w') as file:
            file.write(content)
        print(f"Modified main.dart at {main_dart_path}")
    except Exception as e:
        print(f"Error modifying main.dart: {e}")


if __name__ == "__main__":
    folder_address = input("Enter the folder address (parent of 'lib'): ").strip()

    create_boilerplate_folders(folder_address)
    modify_main_dart(folder_address)
