number = int(input("Enter a number: "))
n, result = number, 1
while True or n :
    result = result * n
    n = n - 1
factorial = result
print("factorial of", number, "is", factorial)