num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    last_digit = num % 10      # gets last digit
    reversed_num = reversed_num * 10 + last_digit  # builds reversed number
    num = num // 10            # removes last digit

print("Reversed:", reversed_num)