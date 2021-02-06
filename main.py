import random

upperCaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCaseChars = "abcdefghijklmnopqrstuvwxyz"
numberChars = "0123456789"
specialChars = "!@#$%^&*()_-+=<>?/{}~|"

upper, lower, number, special = False, False, False, False

all = ""

uppercheck = str(input("Do you want Uppercase Chars in your password? Yes/No "))
if uppercheck == "Yes":
    upper = True

lowercheck = str(input("Do you want Lowercase Chars in your password? Yes/No "))
if lowercheck == "Yes":
    lower = True

numbercheck = str(input("Do you want Numbers in your password? Yes/No "))
if numbercheck == "Yes":
    number = True

specialcheck = str(input("Do you want Special Chars in your password? Yes/No "))
if specialcheck == "Yes":
    special = True

if upper:
    all += upperCaseChars
if lower:
    all += lowerCaseChars
if number:
    all += numberChars
if special:
    all += specialChars

length = int(input("Length of password: "))
amount = int(input("Amount of passwords: "))

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
