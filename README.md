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

