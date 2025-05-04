# Find all white spaces of a string.
import re

text = input("Enter a string: ")

pattern = r"\s"

whitespaces = re.findall(pattern, text)

print("White spaces found in the string:", whitespaces)
print("Total white spaces:", len(whitespaces))
