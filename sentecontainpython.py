# Check if sentence containing ‘Python’ 
import re

sentence = input("Enter a sentence: ")

pattern = r"Python"

if re.search(pattern, sentence):
    print("The sentence contains 'Python'")
else:
    print("The sentence does not contain 'Python'")

print(re.search(pattern, sentence))