# For loop basics

for i in range(5):
    print("Number:", i)

# range with start and end
for i in range(1, 6):
    print("Number:", i)

# Multiplication table using for loop
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "×", i, "=", num * i)

# Problem 1 — Sum of first n numbers

n = int(input("Enter a number: "))

sum_n = n * (n + 1) // 2

print("Sum =", sum_n)

for i in range(2, 51, 2):
    print(i)


# Star Pattern Program

for i in range(1, 6):
    print("*" * i)