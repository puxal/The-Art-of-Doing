# Challenge 3: The Temperature Conversion Application

print("Welcome to the Temperature Conversion Application")
temp_f = float(input("\nWhat is the given temperature in Fahrenheit?: "))

#convert temp
temp_c = (5/9)*(temp_f - 32)
temp_k = temp_c + 273.15

#round temp

temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)
temp_k = round(temp_k, 4)

#print statements
print("\nstring concatenation\n")
print("Degrees in F:\t" + str(temp_f))
print("Degrees in C:\t" + str(temp_c))
print("Degrees in K:\t" + str(temp_k))

print("\nf-string function\n")
print(f"Degrees in F:\t {temp_f}")
print(f"defgrees in C:\t {temp_c}")
print(f"Degrees in K:\t {temp_k}\n")

print("\n.format function\n")
print("""Degrees in F:\t {0}
Degrees in C:\t {1}
Degrees in K:\t {2}""".format(temp_f, temp_c, temp_k))
