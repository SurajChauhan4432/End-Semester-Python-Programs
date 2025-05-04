# Find all digits in a string. 
import re

text = input("Enter a string: ")

pattern = r"\d"

digits = re.findall(pattern, text)

print("Digits found in the string:", digits)
