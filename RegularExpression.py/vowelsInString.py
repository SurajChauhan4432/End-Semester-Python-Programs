# Find all vowels of a string.
import re

text = input("Enter a string: ")

pattern = r"[aeiouAEIOU]"

vowels = re.findall(pattern, text)

print("Vowels found in the string:", vowels)
