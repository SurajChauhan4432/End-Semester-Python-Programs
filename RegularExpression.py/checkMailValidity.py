# Check mail is valid or not.
import re

pattern = r'\w+@[a-zA-Z]+\.com'

data = "akash@gmail.comkamal267@outlook.comdeepak367@yahoo.comraghav27627@mail34.com"

matches = re.findall(pattern,data)

print("Valid Mails:",matches)
