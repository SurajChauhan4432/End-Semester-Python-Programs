# Find all words ranging from 2 to 4. 
import re

text = input("Enter a string: ")

pattern = r"\b\w{2,4}\b"

words = re.findall(pattern, text)

print("Words with length 2 to 4:", words)
