import os

import pyperclip


def create_files(folder_path, name, initiateProvider: bool):
    # Paths for the 'ui' and 'providers' directories
    ui_folder_path = os.path.join(folder_path, 'ui')
    providers_folder_path = os.path.join(folder_path, 'providers')

    # Ensure that the 'ui' and 'providers' directories exist
    if not os.path.exists(ui_folder_path):
        os.makedirs(ui_folder_path)
    if not os.path.exists(providers_folder_path):
        os.makedirs(providers_folder_path)

    # Deducing file names from the given name
    ui_file_name = f"{name}_screen.dart"
    provider_file_name = f"{name}_provider.dart"

    # Complete paths for the new files
    ui_file_path = os.path.join(ui_folder_path, ui_file_name)
    provider_file_path = os.path.join(providers_folder_path, provider_file_name)

    # Create and open the 'update_request_screen.dart' file
    with open(ui_file_path, 'w') as ui_file:
        ui_file.write(
            f'''import 'package:provider/provider.dart';\nimport 'package:flutter/material.dart';\nimport '../providers/{name}_provider.dart';
class {getCamelCase(name)}Screen extends StatelessWidget {{
 {getCamelCase(name)}Screen({{super.key}});
  ''')

    with open(ui_file_path, 'a') as ui_file:
        if initiateProvider:
            ui_file.write(
                f'@override\nWidget build(BuildContext context) {{\nreturn ChangeNotifierProvider(\ncreate: (_) => {getCamelCase(name)}Provider(),\nchild: Consumer<{getCamelCase(name)}Provider>(\nbuilder: (context, provider, child) {{\nreturn Scaffold(\nbody: OrientationBuilder(\nbuilder: (context, orientation) {{\nif (orientation == Orientation.portrait) {{\nreturn mobileUi();\n}} else {{\nreturn webUi();\n}}\n}},\n),\n);\n}},\n),\n);\n}}\n')

    with open(ui_file_path, 'a') as ui_file:
        ui_file.write(f'''Widget mobileUi() {{
    return Container();
  }}

  Widget webUi() {{
    return Container();
  }}
     }}
''')

    # Create and open the 'update_request_provider.dart' file
    with open(provider_file_path, 'w') as provider_file:
        provider_file.write(
            f'''import 'package:flutter/foundation.dart';\nclass {getCamelCase(name)}Provider extends ChangeNotifier {{}}\n''')

    print(f"Files '{ui_file_name}' and '{provider_file_name}' were created successfully.")


def getCamelCase(name):
    words = name.split("_")
    camelCaseWords = []
    for word in words:
        camelCaseWords.append(word.capitalize())
    camelCaseName = ''.join(camelCaseWords)
    return camelCaseName


def main():
    folder_address = input("Enter the folder address: ").strip()
    # name = folder_address.split('/')[-1]
    name = input("Enter the name: ").strip()
    initiate_provider = input("Do you want to initiate Provider? (y/n): ")
    create_files(folder_address, name, initiate_provider == 'y')

    pyperclip.copy(f"Navigator.push(context, MaterialPageRoute(builder: (context) => {getCamelCase(name)}Screen()));")


if __name__ == "__main__":
    main()