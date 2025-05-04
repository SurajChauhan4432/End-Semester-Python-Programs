# Check if a sentence ends with ‘Python’.
import re

text = input("Enter a sentence: ")

pattern = r"Python$"

if re.search(pattern, text, re.IGNORECASE):
    print("The sentence ends with 'Python' (case-insensitive).")
else:
    print("The sentence does not end with 'Python'.")

print(re.search(pattern, text, re.IGNORECASE))


  


  
  
