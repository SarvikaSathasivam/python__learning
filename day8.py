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