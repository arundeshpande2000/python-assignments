
def factorial(n):
    if(n <  2):
        return 1

    return n * factorial(n-1)

n1 = int(input("Enter a number: "))
f1 = factorial(n1)

print("Factorial is ",f1)