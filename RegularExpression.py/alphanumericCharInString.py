# Find all alphanumeric characters in a string. 
import re

text = input("Enter a string: ")

pattern = r"[a-zA-Z0-9]"

alphanumeric_chars = re.findall(pattern, text)

print("Alphanumeric characters found in the string:", alphanumeric_chars)
