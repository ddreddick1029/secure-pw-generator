import random
import string

print("Welcome to the Password Generator!")

# ask user for password length requirement
length = int(input("How many characters does your password require?: "))

# initialize character types

lower = string.ascii_lowercase
capitalize = string.ascii_uppercase
nums = string.digits
symbols = string.punctuation

# combine all char types
combine = lower + capitalize + nums + symbols

# randomize character types and add length requirement
randomization = random.sample(combine, length)

# construct the secure password
password = "".join(randomization)

# display password
print(password)

