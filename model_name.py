import pyperclip
def convert_text(input_text):
  """Converts text from CamelCase to snake_case."""
  output_text = ""
  for i, char in enumerate(input_text):
    if char.isupper():
      if i > 0:
        output_text += "_"
      output_text += char.lower()
    else:
      output_text += char
  return output_text


user_input = input("Enter the text: ")
converted_text = convert_text(user_input)
print(converted_text)

pyperclip.copy(converted_text)