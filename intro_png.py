import os

def rename_files_in_directory(directory_path):
    try:
        # List all files in the given directory
        files = os.listdir(directory_path)

        for filename in files:
            # Check if the file is a PNG file and follows the "img_<number>.png" pattern
            if filename.startswith("img") and filename.endswith(".png"):
                # Extract the numeric part from the filename
                number_part = filename[4:-4]
                # Create the new filename
                new_filename = f"intro_ellipse_{number_part}.png"
                # Get the full file paths
                old_file_path = os.path.join(directory_path, filename)
                new_file_path = os.path.join(directory_path, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {filename} -> {new_filename}')
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_directory_path_here' with the actual path to your folder containing the PNG files
directory_path = '/Users/jonathanjohn/StudioProjects/sme_user/assets/images'
rename_files_in_directory(directory_path)