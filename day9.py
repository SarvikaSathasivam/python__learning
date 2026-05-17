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