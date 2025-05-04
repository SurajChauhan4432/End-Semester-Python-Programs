# Find at least one digit from a string.
import re

text = input("Enter a string: ")

pattern = r"\d"

digits = re.findall(pattern, text)

if len(digits) >=1 :
    print("At least one digit found:", digits)
else:
    print("No digits found in the string.")
