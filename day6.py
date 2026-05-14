# Find factorial of a number

num = int(input("Input: "))

factorial = 1

for i in range(num, 0, -1):
    factorial *= i

print("Output:", factorial)

# Check Armstrong Number

num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")