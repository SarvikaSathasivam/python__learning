# ── Problem 1 : Reverse a Number ────────────────────────────
def reverse_number(n):
    reversed_num = 0
    n = abs(n)                        # handle negatives
    while n > 0:
        digit = n % 10                # extract last digit
        reversed_num = reversed_num * 10 + digit
        n //= 10                      # remove last digit
    return reversed_num
 
print("Problem 1 — Reverse a Number")
print(f"  Input : 1234  →  Output : {reverse_number(1234)}")
print()
 
 
# ── Problem 2 : Count Digits ────────────────────────────────
def count_digits(n):
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10
    return count
 
print("Problem 2 — Count Digits")
print(f"  Input : 12345  →  Output : {count_digits(12345)} digits")
print()
 
 
# ── Problem 3 : Sum of Digits ────────────────────────────────
def sum_of_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10               # add last digit
        n //= 10
    return total
 
print("Problem 3 — Sum of Digits")
print(f"  Input : 123  →  Output : {sum_of_digits(123)}  (1+2+3)")
print()
 
 
# ── Problem 4 : Armstrong Number ────────────────────────────
def is_armstrong(n):
    digits = str(n)
    power  = len(digits)              # number of digits = exponent
    total  = sum(int(d) ** power for d in digits)
    return total == n
 
print("Problem 4 — Armstrong Number")
for num in [153, 370, 371, 407, 123]:
    mark = "✅" if is_armstrong(num) else "❌"
    print(f"  {num}  →  {mark}")
print()
 
 
# ── Problem 5 : Palindrome Number ───────────────────────────
def is_palindrome(n):
    return n == reverse_number(n)     # reuse Problem 1
 
print("Problem 5 — Palindrome Number")
for num in [121, 1331, 12321, 123, 1234]:
    mark = "✅" if is_palindrome(num) else "❌"
    print(f"  {num}  →  {mark}")
print()
 
 
# ── Problem 6 : Fibonacci Series ────────────────────────────
def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b               # next = sum of previous two
    return series
 
print("Problem 6 — Fibonacci Series")
print(f"  First 10 numbers : {fibonacci(10)}")
print()
 
 
# ── Problem 7 : Factorial ────────────────────────────────────
def factorial(n):
    result = 1
    for i in range(2, n + 1):        # multiply 2 × 3 × … × n
        result *= i
    return result
 
print("Problem 7 — Factorial")
print(f"  Input : 5  →  Output : {factorial(5)}  (5×4×3×2×1)")
print(f"  Input : 6  →  Output : {factorial(6)}")