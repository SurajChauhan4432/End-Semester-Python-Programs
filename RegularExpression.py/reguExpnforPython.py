# Create common regular expression for python@gmail.com and 
# pyithon3@gmail.com
import re

text = input("Enter an email: ")

pattern = r"py[a-z]*\d?@gmail\.com"

if re.fullmatch(pattern, text, re.IGNORECASE):
    print("The email matches the pattern.")
else:
    print("The email does not match the pattern.")
