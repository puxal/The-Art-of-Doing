# Challenge 1: The Letter Counter Application

# Hello World
print("Welcome to the Letter Counter App")

# Get user input, originally i had the input field titled and stripped in the next fields, i should do it when the input is made
name = input("What is your name?: ").title().strip()
print(f"Hello {name}!" )
print("I will count the number of times that a specifc letter appears in a message.")
message = input("Please enter the message: ")

# Receive input and standardize
message = message.lower()
letter = input("Which letter would you like to count the numbers of?: ")
letter = letter.lower()
number = message.count(letter)


# i made an if ... else statement if the number is 1 or otherwise. this uses f-strings
if number == 1:
    print(f"Thanks {name}, your message has {number} {letter} in it.")
else:
    print(f"Thanks {name}, your message has {number} {letter}'s in it.")
