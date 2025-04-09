try:
    file = open('sample.txt', 'r')
    print('readinng file content: ')
    line_1 = file.readline()
    print('line 1: ',line_1)
    line_2 = file.readline()
    print('line 2: ',line_2)
    file.close()
except:
    print("Error : The file 'sample.txt' was not found.")
