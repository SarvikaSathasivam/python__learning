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

    #sum of digits
    # Python program to find sum of digits

num = int(input("Enter a number: "))

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits =", sum_digits)