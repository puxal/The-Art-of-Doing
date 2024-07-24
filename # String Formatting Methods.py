# String Formatting Methods

name = "Jay"
age = 33
money = 9.75

# print using string concatenation (self taught)
print(name + " is " + str(age) + " and has " + str(money) + " dollars.")

# print using the .format() method (good control)
print("{0} is {1} and has ${2} dollars.".format(name,age,money))

# print using f-string (easy, recently introduced)
print(f"{name} is {age} and has ${money} dollars.")