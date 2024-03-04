import os

def check_path(path):
    if os.path.exists(path):
        print("The path exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("The path does not exist.")

path = input("Enter a path: ")
check_path(path)
