#1
def first():
    
    for i in range(1,11):
        print(i)

first()

"""output is
1
2
3
4
5
6
7
8
9
10
"""
#2
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')
if __name__ == "__main__":
    main()

"""output is
Enter a string to check if it's a palindrome: hii m priyanhsu
"hii m priyanhsu" is not a palindrome."""
#3
def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num

def main():
    try:
        user_input = int(input("Enter a number to check if it's an Armstrong number: "))
        if is_armstrong_number(user_input):
            print(f"{user_input} is an Armstrong number.")
        else:
            print(f"{user_input} is not an Armstrong number.")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()

"""output is
Enter a number to check if it's an Armstrong number: 899448
899448 is not an Armstrong number."""

#4
def generate_fibonacci_up_to(max_value):
    fibonacci_series = []
    a, b = 0, 1
    while a <= max_value:
        fibonacci_series.append(a)
        a, b = b, a + b
        
    return fibonacci_series

def main():
    max_value = 50
    fibonacci_series = generate_fibonacci_up_to(max_value)
    print(f"Fibonacci series between 0 and {max_value}:")
    print(fibonacci_series)
if __name__ == "__main__":
    main()

   """ output is
    Fibonacci series between 0 and 50:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"""

#5
import string

def check_password_validity(password):
    min_length = 8
    special_characters = string.punctuation

def main():
    password = input("Enter your password: ")
    if check_password_validity(password):
        print("Password is valid.")
    else:
        print("Password is invalid. It must be at least 8 characters long and include an uppercase letter, a lowercase letter, a digit, and a special character.")
if __name__ == "__main__":
    main()

output is
"""Enter your password: punit jsh
Password is invalid. It must be at least 8 characters long and include an uppercase letter, a lowercase letter, a digit, and a special character."""
