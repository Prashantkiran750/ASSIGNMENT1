'''
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

'''
dict1 = {"Ram": 82, "Shyam": 90, "Sita": 99, "Gita": 42}
Student = input("Enter student name: ")
if Student in dict1:
    print(f"{Student}'s mark:", dict1[Student])
else:
    print("Student not found.")