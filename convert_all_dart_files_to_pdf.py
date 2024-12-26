import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def convert_dart_to_pdf(dart_file_path, pdf_file_path):
    """Converts a single Dart file to a PDF with plain text content.

    Args:
        dart_file_path (str): Absolute path to the Dart file.
        pdf_file_path (str): Absolute path where the PDF should be saved.
    """
    try:
        with open(dart_file_path, 'r', encoding='utf-8') as f:
            dart_code = f.read()

        # Create the PDF
        c = canvas.Canvas(pdf_file_path, pagesize=letter)
        c.setFont("Courier", 10)  # Choose a suitable font

        textobject = c.beginText(50, 750)
        y_position = 750
        line_height = 12

        for line in dart_code.splitlines():
            textobject.textLine(line)
            y_position -= line_height
            if y_position < 50:
                c.drawText(textobject)
                c.showPage()
                textobject = c.beginText(50, 750)
                y_position = 750

        c.drawText(textobject)
        c.save()

        print(f"Successfully converted '{os.path.basename(dart_file_path)}' to '{os.path.basename(pdf_file_path)}'")

    except FileNotFoundError:
        print(f"Error: Dart file not found at '{dart_file_path}'")
    except Exception as e:
        print(f"Error converting '{os.path.basename(dart_file_path)}': {e}")

def main(dart_file_paths, output_path):
    """Converts a list of specified Dart files to PDFs (plain text).

    Args:
        dart_file_paths (list): A list of absolute paths to the Dart files to convert.
        output_path (str): Absolute path to the folder where PDF files should be saved.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for dart_file_path in dart_file_paths:
        if os.path.isfile(dart_file_path) and dart_file_path.endswith('.dart'):
            pdf_file_name = os.path.splitext(os.path.basename(dart_file_path))[0] + ".pdf"
            pdf_file_path = os.path.join(output_path, pdf_file_name)
            convert_dart_to_pdf(dart_file_path, pdf_file_path)
        else:
            print(f"Skipping invalid Dart file path: '{dart_file_path}'")

if __name__ == "__main__":
    dart_file_paths_input = input("Enter the absolute paths of the Dart files to convert, separated by commas: ")
    pdf_output_directory = input("Enter the absolute path to the folder where you want to save the PDFs: ")

    dart_file_paths = [path.strip() for path in dart_file_paths_input.split(',')]

    if not os.path.isdir(pdf_output_directory):
        print(f"Error: '{pdf_output_directory}' is not a valid directory.")
    else:
        main(dart_file_paths, pdf_output_directory)