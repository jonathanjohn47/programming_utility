import regex as re
import pyperclip


print("Enter your text (press Enter twice to finish):")
input_lines = []
while True:
    line = input()
    if line == "DONE":
        break
    input_lines.append(line)
input_text = "\n".join(input_lines)

# Remove all the contents of square brackets
output_text = re.sub(r'\[.*?\]', '', input_text)

# Remove numbers followed by a period and replace with a period
output_text = re.sub(r'\d+\.', '.', output_text)

# Remove space before a period
output_text = re.sub(r' \.', '.', output_text)
output_text = re.sub(r'([A-Za-z].?)+\d\.', '$1.', output_text)
output_text = re.sub(r'\•', '', output_text)


pyperclip.copy(output_text)

print(output_text)