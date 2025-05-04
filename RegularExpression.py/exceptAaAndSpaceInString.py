# Find all digits, alphabets and special symbols except ‘a’ from string.
import re

text = input("Enter a string: ")

pattern = r"[b-zB-Z\d]|[^a-zA-Z0-9\s]"

matches = re.findall(pattern, text)

print("Matched characters (digits, letters except 'a'/'A', special symbols):", matches)
