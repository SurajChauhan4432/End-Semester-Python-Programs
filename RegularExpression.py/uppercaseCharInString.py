# Find all uppercase characters in a string.
import re

text = input("Enter a string: ")

pattern = r"[A-Z]"

uppercase_letters = re.findall(pattern, text)

print("Uppercase letters found in the string:", uppercase_letters)
