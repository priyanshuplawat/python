#1
start = 10
while start >= 1:
    print(start)
    start -= 1

"""output is
10
9
8
7
6
5
4
3
2
1"""

#2
def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]
while True:
    try:
        number = int(input("Enter a number to check if it is a palindrome: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
if is_palindrome(number):
    print(f"The number {number} is a palindrome.")
else:
    print(f"The number {number} is not a palindrome.")

"""Enter a number to check if it is a palindrome: 121
The number 121 is a palindrome."""


#3
def calculate_factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

while True:
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            print("The number is negative... Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}.")

"""Enter a positive integer: 5
The factorial of 5 is 120."""

#4
sum = 0
while True:
    # Take input from the user
    number = int(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        break
    sum += number
print(f"The sum of all entered numbers is: {sum}")

"""Enter a number (enter 0 to stop): 5
Enter a number (enter 0 to stop): 6
Enter a number (enter 0 to stop): 2
Enter a number (enter 0 to stop): 0
The sum of all entered numbers is: 13"""


  
    
