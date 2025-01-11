import os
import sys
from fpdf import FPDF


def find_php_files(directory_path):
    """
    Recursively traverses a directory and returns a list of PHP files with their relative paths.

    Args:
      directory_path: The absolute path of the directory to search.

    Returns:
        A list of tuples, where each tuple contains (relative_path, absolute_path) for each PHP file found.
        Returns an empty list if no files are found or if an error occurs.
    """
    php_files = []
    try:
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith(".php"):
                    absolute_path = os.path.join(root, file)
                    relative_path = os.path.relpath(absolute_path, directory_path)
                    php_files.append((relative_path, absolute_path))
    except Exception as e:
        print(f"Error during directory traversal: {e}")
        return []
    return php_files


def read_php_file(file_path):
    """
    Reads the content of a PHP file.

    Args:
        file_path: The absolute path to the PHP file.

    Returns:
        The content of the file as a string, or None if an error occurs.
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def create_pdf_from_php_files(php_files, output_pdf_path):
    """
    Creates a PDF document containing the content of PHP files.

    Args:
      php_files: A list of tuples with relative and absolute path.
      output_pdf_path: The path where the PDF will be saved.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=10)

    for relative_path, absolute_path in php_files:
        pdf.set_font("Courier", style="B", size=12)
        pdf.cell(200, 10, txt=f"File: {relative_path}", ln=True)
        pdf.set_font("Courier", style="", size=10)

        content = read_php_file(absolute_path)
        if content:
            for line in content.splitlines():
                pdf.cell(200, 5, txt=line, ln=True)
            pdf.ln(3)  # add some space between files
        else:
            pdf.cell(200, 5, txt="--- COULD NOT READ FILE CONTENT ---", ln=True)
            pdf.ln(3)  # add some space between files

    try:
        pdf.output(output_pdf_path)
        print(f"PDF saved successfully to {output_pdf_path}")
    except Exception as e:
        print(f"Error generating PDF: {e}")


def main():
    """
    Main function to take the directory path from user input, handle input, and start the process.
    """
    directory_path = input("Enter the absolute path of the directory containing PHP files: ")

    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)

    php_files = find_php_files(directory_path)
    if not php_files:
        print(f"No PHP files found in {directory_path}.")
        sys.exit(0)

    output_pdf_path = os.path.join(directory_path, "concatenated_php.pdf")
    create_pdf_from_php_files(php_files, output_pdf_path)


if __name__ == "__main__":
    main()