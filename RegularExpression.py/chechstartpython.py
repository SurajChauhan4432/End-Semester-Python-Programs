# Check if sentence starts with ‘Python’
import re

sentence = input("Enter a sentence: ")

pattern = r"^Python"

if re.match(pattern, sentence):
    print("The sentence starts with 'Python'")
else:
    print("The sentence does not start with 'Python'")

print(re.match(pattern, sentence))
