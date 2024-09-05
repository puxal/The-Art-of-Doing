# quadratic equation
import cmath
# summary
print('a quadratic equation is of the for ax^2 + bx + c = 0\nyour solutions can be real or complex numbers.\na complex number has two parts: a + bj')
print('where a is the real portion and bj is the imaginary portion\n\n')

#get user input

eq_num = int(input('how many equations would you like to solve today: ')) #convert to int for looping


for i in range(eq_num):
    print("\n\tSolving Equation #" + str(i+1)+"\n---------------------------")
    a = float(input('pleae enter your value of a (coeffiient of x^2): '))
    b = float(input('pleae enter your value of b (coeffiient of x): '))
    c = float(input('pleae enter your value of c (coeffiient): '))
    #solving the quadratic equation
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
1
print('\nthe solution to ' + str(a) + "x^2 + " + str(b) + "x + " + str(c) +  " = 0")
print("\n\tx1 = " + str(x1))
print('\tx2 = ' + str(x2))

print('\nthanks for using the quadratic equation solver app!')
