import pyperclip

def format_addresses_and_copy():
    """
    Asks the user for absolute addresses, one per line, formats them,
    prints them, and copies the formatted output to the clipboard.
    """
    print("Enter the absolute addresses, one per line. Press Enter twice to finish:")
    absolute_addresses = []
    while True:
        address = input()
        if not address:  # An empty line signals the end of input
            break
        absolute_addresses.append(address)

    formatted_addresses = []
    for i, address in enumerate(absolute_addresses):
        formatted_address = f'"{address}'
        if i < len(absolute_addresses) :
            formatted_address += '",'
        formatted_addresses.append(formatted_address)

    # Join the formatted addresses with newline characters
    all_formatted_addresses = "\n".join(formatted_addresses)

    print("\nFormatted addresses:")
    print(all_formatted_addresses)

    try:
        pyperclip.copy(all_formatted_addresses)
        print("\nFormatted addresses copied to clipboard!")
    except pyperclip.PyperclipException:
        print("\nCould not copy to clipboard. Make sure you have pyperclip installed.")
        print("You can install it using: pip install pyperclip")

if __name__ == "__main__":
    format_addresses_and_copy()