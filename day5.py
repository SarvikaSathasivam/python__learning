# While loop

count = 1
while count <= 5:
    print("Count is:", count)
    count = count + 1

print("Loop finished!")

# Multiplication table
num = int(input("Enter a number for multiplication table: "))
i = 1
while i <= 10:
    print(num, "×", i, "=", num * i)
    i = i + 1




# Sum of numbers using while loop
num = int(input("Enter a number: "))
i = 1
total = 0
while i <= num:
    total = total + i
    i = i + 1
print("Sum of 1 to", num, "is:", total)

# Guess the number game
secret = 7
guess = int(input("Guess the secret number between 1 and 10: "))

while guess != secret:
    if guess < secret:
        print("Too low! Try again")
    else:
        print("Too high! Try again")
    guess = int(input("Guess again: "))

print("Correct! You guessed it! 🎉")