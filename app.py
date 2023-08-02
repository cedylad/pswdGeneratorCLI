import random

# Define character sets for the password generation with uppercase and lowercase letters, numbers and symbol
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbol = "@[]#$())*+.:;{}|~?"

# Combine all character sets into one for password generation
character = letter + letter.lower() + number + symbol

# Password generation loop
while True:
    len_password = int(input("Password length: "))  # Ask for the desired password length
    pswd = ''.join(random.choice(character) for _ in range(len_password))  # Generate the password
    print("Generated password:", pswd)  # Display the generated password
