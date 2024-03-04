import os

path = "../"  # . refers to the current directory, .. to the parent dir, / used to separate directories
dir_list = os.listdir(path) 

print("Directories in '", path, "' :")  
for item in dir_list:
    if os.path.isdir(os.path.join(path, item)):
        print(item)

print("\nFiles in '", path, "' :")  
for item in dir_list:
    if os.path.isfile(os.path.join(path, item)):
        print(item)

print("\nAll directories and files in '", path, "' :")  
for item in dir_list:
    print(item)
