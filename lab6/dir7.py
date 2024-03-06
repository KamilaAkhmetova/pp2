import os

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

if os.path.exists(source_file):
    copy_file(source_file, destination_file)
else:
    print("Source file not found.")
