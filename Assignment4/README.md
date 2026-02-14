# ASSIGNMENT3

#Task1
=> Used 'try' and 'except' block
=> Inside 'try' block , file named sample.txt was opened in read only mode and assign to content variable . All lines are read using 'content.readlines' function 
=> This will give output as data type list
=> Now, we use for loop to print each item(line) from list(lines). Inside print function, we use 'lines.index(line)+1' to print index and incremented it by 1 . The 'line.rstrip('\n')' is used to remove '\n' from each line
=> The file is then closed
=> Then 'except FileNotFoundError:' is used to handle error gracefully if file 'sample.txt' does not present
#Task2
=> File 'output.txt' is opened in 'append' mode and assign it to fh
=>The file is then used to write the input from the user
=> 'fh.write("\n")' is used so that any further input from user will be added in next line
=> File is the again opened in append mode and assign to variable 'file'
=> 'user_input' will ask user to enter additinal data and the it will be appneded to next line in the file
=> Finally, all the content of the file is printed with print(content)

