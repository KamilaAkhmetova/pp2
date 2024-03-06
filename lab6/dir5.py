import os

def write_list_to_file(file_name, my_list):
    try:
        with open(file_name, 'w') as file:
            for item in my_list:
                file.write("%s\n" % item)
        print("List has been written to", file_name)
    except Exception as e:
        print("An error occurred:", str(e))

my_list = ["apple", "banana", "orange", "grape"]
file_name = input("Enter the file name: ")

if os.path.exists(file_name):
    print("File already exists. Do you want to overwrite it? (yes/no)")
    overwrite = input().lower()
    if overwrite == "yes":
        write_list_to_file(file_name, my_list)
    else:
        print("Operation aborted.")
else:
    write_list_to_file(file_name, my_list)
