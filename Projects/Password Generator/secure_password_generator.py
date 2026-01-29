import random
import string
print("Secure Password Generator")
length =int(input("enter the length of password: "))
numbers=input("Includes numbers (Y/N): ").upper()
symbols=input("Includes symbol (Y/N): ").upper()
characters=string.ascii_letters # a-z+ A-Z
if numbers=="Y":
    characters=characters+string.digits #0-9
if symbols=="Y":
    characters=characters+string.punctuation  #@!#$%
password=""
for _ in range(length):
    password+=random.choice(characters)
print(f"Generated secure password:{password}")