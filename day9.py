# Lists in Python

fruits = ["apple", "banana", "mango", "orange", "grapes"]

# Accessing elements
print(fruits[0])      # first element
print(fruits[2])      # third element
print(fruits[-1])     # last element

# Length of list
print("Total fruits:", len(fruits))

# Adding to list
fruits.append("pineapple")
print("After adding:", fruits)

# Removing from list
fruits.remove("banana")
print("After removing:", fruits)

# Loop through list
print("All fruits:")
for fruit in fruits:
    print(fruit)

# Check if item exists
if "mango" in fruits:
    print("Mango is in the list!")


numbers = [34, 67, 23, 89, 45, 12, 90, 56]

# Assume first number is the largest
largest = numbers[0]

# Loop through the list
for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

# Loop through the list
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)


numbers = [1, 2, 3, 4, 5]

reversed_list = []

# Loop backwards through the list
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)