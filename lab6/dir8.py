import os

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print("File deleted successfully.")
            else:
                print("You do not have permission to delete this file.")
        else:
            print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

file_path = input("Enter the file path to delete: ")
delete_file(file_path)
