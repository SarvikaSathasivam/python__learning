# Conditions in Python

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor")
elif age >= 18 and age <= 60:
    print("You are an adult")
else:
    print("You are a senior citizen")

# Grade checker
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F - Please study harder!")