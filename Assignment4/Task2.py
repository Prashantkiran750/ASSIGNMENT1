'''
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
import io
fh = open("output.txt","a")
fh.write(input("Enter text to write to the file: "))
print("Data successfully written to the output.txt.")
fh.write("\n")
print()
fh.close()
# print("Data successfully written to the output.txt.")
file = open("output.txt","a")
user_input = input("Enter additional text to append: ")
file.write(user_input)
file.close()
print("Data successfully appended.")
print()
print("Final content of output.txt:")
fh2 = open("output.txt","r")
content = fh2.read()
print(content)
fh2.close()

