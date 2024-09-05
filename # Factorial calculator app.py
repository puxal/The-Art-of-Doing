# Factorial calculator app
import math

print('Welcome to the factorial calcultor app')

number = int(input('What number would you like to compute the factorial of?: '))


print("\n" + str(number) + "! = ", end="" )
for i in range(1, number): # i is the range from 1 to input 
    print(str(i), end="*")
print(str(number))

#using the math library
fact = math.factorial(number) #very easy way to make this happen
print('\nHere is the result from the Math library: ')
print('The factorial of ' + str(number) + " is " + str(fact) + "!")

#my own algorihm
fact = 1
for i in range(1, number+1): #range does not include the final number, add one to make this correct
    fact = fact*i # for loop every value in range to be multiplied by the value before it

print('\nHere is the result from my own algorithm: ')
print('The factorial of ' + str(number) + " is " +str(fact))
print('\nIt is shown twice that ' + str(number) + "! = " + str(fact)+"!")