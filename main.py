# letter counter app

print("welcome to my letter counter app")

# get userinput
name = input("\nwhat is your name?: ").title().strip()
print("Hello, " + name + "!")

print("I will count the specific number of times a letter appears in a message.")
message = input("What is the message?: ")
letter = input("Which letter would you like to count?:")

# standardized to lowercase
message = message.lower()
letter = letter.lower()

letter_count = message.count(letter)

print("Thanks, " + name + ". your message has " + str(letter_count) + " " + letter + "'s in it.")