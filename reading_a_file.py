# read through a file and print the content line by line in upper case.

# ask for the files to be opened 
file_name = input("Enter the file name to be opened: ")

# use try and except to avoid bad input
try:
    # open the file in a read mode
    open_file = open(file_name, "r")
except:
    print("This file cannot be opened:", file_name)
    quit()
    

# read the file content
read_file = open_file.read()

# print the file content in upper case
print(read_file.upper())