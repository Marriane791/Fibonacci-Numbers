import math

userInput = int(input("Enter the number you wish to test:"))

# test the number if it is a perfect square ie its square root is an integer
def perfectSquare(x):
    num = int(math.sqrt(x))
    return num * num == x

# a function to test if the number is a fibonacci number
def isFibonacci(n):
    return perfectSquare(5*n*n + 4) or perfectSquare(5*n*n - 4)

#check if true
if (isFibonacci(userInput)== True):
    print(f'{userInput} is a fibonacci number')
else:
    print(f'{userInput} is not a fibonacci number')