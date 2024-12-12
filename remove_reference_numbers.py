import re
import sys

import pyperclip


def main():
    print("Enter your paragraphs below.")
    print("When you're finished, press Ctrl+D (Unix/Linux/macOS) or Ctrl+Z followed by Enter (Windows) to submit.\n")

    try:
        # Read multi-line input from the user until EOF is encountered
        user_input = sys.stdin.read()
    except KeyboardInterrupt:
        # Handle cases where the user might interrupt the input
        print("\nInput interrupted by user.")
        sys.exit(0)

    # Debug: Show the original input (optional)
    # print("\nOriginal Text:")
    # print(user_input)

    # Use regex to replace ".<number>" with "."
    cleaned_text = re.sub(r'\.\d+', '.', user_input)

    print("\nCleaned Text:")
    print(cleaned_text)

    pyperclip.copy(cleaned_text)

if __name__ == "__main__":
    main()
