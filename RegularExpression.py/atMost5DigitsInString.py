# Find at most five digits of a string.
import re

text = input("Enter a string: ")

pattern = r"\d"

digits = re.findall(pattern, text)

at_most_five_digits = digits[:5]

print("At most five digits found in the string:", at_most_five_digits)
