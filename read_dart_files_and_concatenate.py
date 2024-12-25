import os

import pyperclip


def concatenate_dart_files(file_paths):
    """
    Reads through a list of Dart files and concatenates their content
    in the specified format.

    Args:
        file_paths: A list of absolute paths to the Dart files.

    Returns:
        A string containing the concatenated content of the Dart files
        formatted with triple backticks.
    """
    concatenated_content = ""
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                concatenated_content += f"```\n{content}\n```\n"
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
    return concatenated_content


if __name__ == "__main__":
    # Example usage:
    dart_files = [
        "/Users/jonathanjohn/StudioProjects/matrimonial_flutter_app/lib/screens/user_pages/public_profile_action.dart",
        "/Users/jonathanjohn/StudioProjects/matrimonial_flutter_app/lib/screens/user_pages/public_profile_middleware.dart",
        "/Users/jonathanjohn/StudioProjects/matrimonial_flutter_app/lib/screens/user_pages/public_profile_reducer.dart",
        "/Users/jonathanjohn/StudioProjects/matrimonial_flutter_app/lib/screens/user_pages/public_profile_state.dart"
        "/Users/jonathanjohn/StudioProjects/matrimonial_flutter_app/lib/screens/user_pages/user_gallery/ui/user_gallery.dart",
        "/Users/jonathanjohn/StudioProjects/matrimonial_flutter_app/lib/screens/user_pages/user_gallery/get_controllers/user_gallery_get_controller.dart"

    ]

    concatenated_content = concatenate_dart_files(dart_files)
    print(concatenated_content)
    pyperclip.copy(concatenated_content)
