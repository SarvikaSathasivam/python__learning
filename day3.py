name = input ("may i know your good name?!")
age = input ("how young aree you?!")
city = input ("where are you from?")

print("hello", name)
print("i am", age ,"years young")
print("i am from",city)

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
sum = num1 + num2
print("sum of ",num1,"and",num2, "is",sum)

#simple interest:
p = int(input("enter the principal amount:"))
r = float(input("enter the r value:"))
t = int(input("enter the time duration:"))

si = (p*r*t)/100
print("simple interest is",si)

#swapping
a = int(input("give the a value:"))
b = int(input("give the b value:"))
temp = a 
a = b
b = temp
print(" the value of a now is ",a,".","the value of b now is",b)

a,b = b, a 
print(a,b)

