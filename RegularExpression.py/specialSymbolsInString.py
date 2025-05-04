# Find all special symbols of a string.
import re

text = input("Enter a string: ")

pattern = r"[^a-zA-Z0-9\s]"

special_symbols = re.findall(pattern, text)

print("Special symbols found in the string:", special_symbols)
