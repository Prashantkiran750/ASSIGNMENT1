'''
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.

'''

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

Addition = first_number + second_number
Subtraction = first_number - second_number
Multiplication = first_number * second_number
Division = first_number / second_number
print("Addition: ", Addition)
print("Subtraction: ", Subtraction)
print("Multiplication: ", Multiplication)
print("Division: ", Division)