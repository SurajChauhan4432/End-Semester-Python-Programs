# Create a common regular expression for 123-456-7890 and 1121451617
import re

text = input("Enter a phone number: ")

pattern = r"(\d{3}-\d{3}-\d{4}|\d{10})"

print("Using pattern:", pattern)

if re.fullmatch(pattern, text):
    print("The phone number matches the pattern.")
else:
    print("The phone number does not match the pattern.")
