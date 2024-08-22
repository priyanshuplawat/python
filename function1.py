#1
def div(a,b):
 c=a/b
 print("the division is ",c)

div(20,5)

"""the division is  4.0"""

#2
def square(a):
    b=(a**2)
    print("the square is ",b)

square(5)

"""the square is  25"""

#4
name = input("Please enter your name: ")
lowercase_name = name.lower()
print("Your name in lowercase is:", lowercase_name)

"""Please enter your name: PRIYANSHU
Your name in lowercase is: priyanshu"""

#3
import random

numbers = [random.randint(1, 100) for _ in range(5)]
max_num = max(numbers)
min_num = min(numbers)
print(f"Numbers: {numbers}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")

"""Numbers: [64, 40, 36, 22, 72]
Maximum: 72
Minimum: 22"""









    
  
