# Find factorial of a number

num = int(input("Input: "))

factorial = 1

for i in range(num, 0, -1):
    factorial *= i

print("Output:", factorial)