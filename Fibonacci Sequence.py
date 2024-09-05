# For Loop Challenge 14: Fibonacci Sequence

print("how many digits of the fibonacci squence would you like to compute?")

#get user input
num = int(input('how many digits of the fibonacci sequence would you like to compute?: '))

#compute the values of the fib
fib = [1,1]
for i in range(num-2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)

print(int(fib))