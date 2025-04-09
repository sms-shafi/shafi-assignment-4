# ASSIGNMENT - 4
---
# Task 1: Read a File and Handle Errors

# code:
```
try:
# this block is used to try running code that might cause an error.

    file = open('sample.txt', 'r')
# This line tries to open a file named sample.txt in read mode 'r'

    print('readinng file content: ')
# Just a simple message printed to let the user know that file reading is starting.

    line_1 = file.readline()
# Reads the first line from the file and stores it in the variable line_1

    print('line 1: ',line_1)
# Prints the first line from the file.

    line_2 = file.readline()
#Reads the second line from the file and stores it in line_2

    print('line 2: ',line_2)
# Prints the second line read from the file.

    file.close()
# Closes the file.

except:
# This block runs only if an error

    print("Error : The file 'sample.txt' was not found.")
# This message is shown if the file is missing
```
---
# Task 2: Write and Append Data to a File

# code
```
file = open('output.txt', 'w')
# this line is used to open or create file in  write mode 'w'

output_file = file.write(input('Enter text to write the file: ') + '\n')  
# Takes user input and writes it to the file, adds a newline \n

file.close()
# it close the file

print('Data successfully written to output.txt.\n')
# Confirmation message

file_2 = open('output.txt', 'a')
# 'a' means append mode it adds content without deleting existing.

appending_file = file_2.write(input('Enter additional text to append: ') + '\n')  
# Takes another input frome user

file_2.close()
# Close the file again

print('Data successfully appended.\n')
 # Confirmation message

file_3 = open('output.txt', 'r')
# it opens the file in read mode and reads the entire file

print('Final content of output.txt: ')
#print a message for users

output_file = file_3.read()
# Reads the full content of the file and stores in variable

print(output_file)
# Prints contant inside the file

file_3.close()
# Finally, close the file


