# Find all consonants of a string.
import re

text = input("Enter a string: ")

pattern = r"[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]"

consonants = re.findall(pattern, text)

print("Consonants found in the string:", consonants)
