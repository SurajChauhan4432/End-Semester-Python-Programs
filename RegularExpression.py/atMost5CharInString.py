# Find at most five characters of a string. 
import re

text = input("Enter a string: ")

pattern = r"."

chars = re.findall(pattern, text)

at_most_five = chars[:5]

print("At most five characters found in the string:", at_most_five)
