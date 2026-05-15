num = int(input("Enter a number: "))
result = 1
i = 1

while i <= num:
    result = result * i
    i = i + 1

print("Factorial:", result)