import pyperclip
import regex as re

print("Enter your text (press Enter twice to finish):")
input_lines = []
while True:
    line = input()
    if line == "":
        break
    input_lines.append(line)
input_text = "\n".join(input_lines)
# remove all the contents of square brackets
output_text = re.sub(r'\[.*?\]', '', input_text)

pyperclip.copy(output_text)

print(output_text)
