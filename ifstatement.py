#1.
number = int(input("enter a number "))
if number%2==0:
    print("number is even")
else:
    print("number is odd")

"""enter a number 5
number is odd,
enter a number 6
number is even"""
#2.
age = float(input("Enter your age "))
if (age>=18):
    print("you are eligible for vote")
else:
    print("you are not eligible for vote") 
             

"""Enter your age12
you are not eligible for vote"""

"""Enter your age 19
you are eligible for vote"""
#3.
days = int(input("Enter year's days "))
if days == 366:
    print("This is a leap year")
else:
    print("This is not a leap year")


"""Enter year's days 365
This is not a leap year """


"""Enter year's days 366
This is a leap year"""
#4.
number = float(input("Enter a number "))
if (number>0):
    print("Number is positive")
elif (number == 0):
    print("Number is equal to zero")
else :
    print("Number is negative")


"""Enter a number 5
Number is positive,
Enter a number 0
Number is equal to zero,
Enter a number -5
Number is negative"""
#5
a = float(input("enter number 1st "))
b = float(input("enter number 2nd "))
c = float(input("emter number 3rd "))
if a>=b and a>=c:
    print("B is grater")
elif b>=c and b>=a:
    print("B is grater")
else :
    print("C is grater")
          


"""enter number 1st 5
enter number 2nd 3
emter number 3rd 8
C is grater"""



