'''
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its
     factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''

number = int(input("Enter a number: "))
def factorial(number):
    num = 1
    while number > 1:
        num *= number
        number -= 1

    return num

print(f"Factorial of {number} is: ",factorial(number))










