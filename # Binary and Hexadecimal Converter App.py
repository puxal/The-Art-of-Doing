# Binary and Hexadecimal Converter App

print("welcome to the binary/hexadecimal conversion app")
max_value = int(input("\ncompute binary and hexadecimal values upto the following decimal point: "))
decimal = list(range(1, max_value+1))
binary = [] #base 2 bin(*)
hexadecimal = [] #base 16 hex(*)
for num in decimal: # decimal is already populated from max_value input
    binary.append(bin(num)) # append to the binary list the binary value of num
    hexadecimal.append(hex(num)) # append to the hexa list the 16 base value of num
print("Generating lists...\n Complete.")

#get slicing index from user
print("\nUsing Slices we will now show a portion of each list.")
lower_range = int(input("what decimal number woud you like to start at?"))
upper_range = int(input("what decimal number woud you like to end at?"))

# Slice through each list individually
print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")
for num in decimal[lower_range-1:upper_range]:
    print(num)

print("\nBinary values from " + str(lower_range) + " to " + str(upper_range) + ":")
for num in binary[lower_range-1:upper_range]:
    print(num)

print("\nHexadecimal values from" + str(lower_range) + " to " + str(upper_range) + ":")
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)

    #output the whole list to the screen

input("\nPress enter to see all values from 1 to " + str(max_value) + ".")
print("\nDecimal----Binary----Hexadecimal")
print("---------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "----" + str(b) + "----" + str(h))
