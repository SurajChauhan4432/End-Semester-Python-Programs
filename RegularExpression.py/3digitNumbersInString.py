# Find all three digit numbers in a string.
import re

text = input("Enter a string: ")

pattern = r"\b\d{3}\b"

three_digit_numbers = re.findall(pattern, text)

print("Three-digit numbers found in the string:", three_digit_numbers)
