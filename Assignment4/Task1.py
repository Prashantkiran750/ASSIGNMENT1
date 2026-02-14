'''
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

try:
    content = open("sample.txt", "r")
    lines = content.readlines()
    print("Reading file content:")
    for line in lines:
        print(f"Line {lines.index(line)+1}:",line.rstrip('\n'))
    content.close()
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")

