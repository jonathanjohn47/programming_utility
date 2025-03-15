import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf_from_content(combined_content, pdf_file_path):
    """Creates a PDF from the given text content.

    Args:
        combined_content (str): The combined text content of the Dart files.
        pdf_file_path (str): Absolute path where the PDF should be saved.
    """
    try:
        # Create the PDF
        c = canvas.Canvas(pdf_file_path, pagesize=letter)
        c.setFont("Courier", 10)  # Choose a suitable font

        textobject = c.beginText(50, 750)
        y_position = 750
        line_height = 12

        for line in combined_content.splitlines():
            textobject.textLine(line)
            y_position -= line_height
            if y_position < 50:
                c.drawText(textobject)
                c.showPage()
                textobject = c.beginText(50, 750)
                y_position = 750

        c.drawText(textobject)
        c.save()

        print(f"Successfully created PDF: '{os.path.basename(pdf_file_path)}'")

    except Exception as e:
        print(f"Error creating PDF '{os.path.basename(pdf_file_path)}': {e}")

def main(lib_directory_path, output_path):
    """Walks through the lib directory, concatenates Dart files, and creates a single PDF.

    Args:
        lib_directory_path (str): Absolute path to the 'lib' directory.
        output_path (str): Absolute path to the folder where the PDF should be saved.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    combined_dart_code = ""
    dart_files_found = False

    for root, _, files in os.walk(lib_directory_path):
        for file in files:
            if file.endswith('.dart') or file.endswith('.php'):
                dart_file_path = os.path.join(root, file)
                try:
                    with open(dart_file_path, 'r', encoding='utf-8') as f:
                        dart_code = f.read()
                        combined_dart_code += f"```\nContent of {os.path.relpath(dart_file_path, lib_directory_path)}\n```\n"
                        combined_dart_code += dart_code + "\n\n"  # Add separator
                        dart_files_found = True
                except Exception as e:
                    print(f"Error reading '{dart_file_path}': {e}")

    if dart_files_found:
        pdf_file_name = input("Enter the name of the PDF file (without extension): ")
        pdf_file_path = os.path.join(output_path, f"{pdf_file_name}.pdf")
        create_pdf_from_content(combined_dart_code, pdf_file_path)
    else:
        print(f"No Dart files found in '{lib_directory_path}' or its subdirectories.")

if __name__ == "__main__":
    lib_directory = input("Enter the absolute path to the 'lib' directory: ")
    pdf_output_directory = input("Enter the absolute path to the folder where you want to save the PDF: ")

    if not os.path.isdir(lib_directory):
        print(f"Error: '{lib_directory}' is not a valid directory.")
    elif not os.path.isdir(pdf_output_directory):
        print(f"Error: '{pdf_output_directory}' is not a valid directory.")
    else:
        main(lib_directory, pdf_output_directory)