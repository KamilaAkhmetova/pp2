import os

def count_lines(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return len(lines)
    else:
        print("File not found.")
        return -1  # Return -1 to indicate error

file_name = input("Enter the file name: ")
line_count = count_lines(file_name)
if line_count != -1:
    print("Number of lines in the file:", line_count)
