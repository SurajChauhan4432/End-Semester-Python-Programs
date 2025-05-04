# Find at least two alphanumeric characters of a string.

import re

text = input("Enter a string: ")

pattern = r"[a-zA-Z0-9]"

matches = re.findall(pattern, text)

if len(matches) >= 2:
    print("At least two alphanumeric characters found:", matches)
else:
    print("Less than two alphanumeric characters found")
