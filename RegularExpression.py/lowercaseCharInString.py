# Find all uppercase characters in a string.
import re

text = input("Enter a string: ")

pattern = r"[a-z]"

lowercase_letters = re.findall(pattern, text)

print("Lowercase letters found in the string:", lowercase_letters)
