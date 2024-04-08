# Course: IT1114/Section 01
# Student Name: Garrett Cook
# Assignment Number: Lab9
# Due Date: 04/9/2024
# Purpose:Write a program that will verify a password
password = input("Password:")
length = low = up = digit = symbol = False
char = '$','_','!','#'

#checks if lenght meets requirements
if len(password) >= 9 :
    length =  True
    #while length is true we continue to check other attributes of the users input.i i s each letter in their inputted password.
    for i in password:
        if i.isupper():
            up = True
        elif i.islower():
            low = True
        elif i.isdigit():
            digit = True
        #no function for char so we just check if anny i contians one of the special characters from our method above.
        elif i in char:
            symbol = True
if length and low and up and digit and symbol:  # once everything is True/checked then we know it's a valid password.
    print("Valid password")
else:#if not true then we know it's invalid.
    print("Invalid password")

