import os 
   
# Get the list of all files and directories 
path = "../" # . refers to the current directory, .. to the parent dir, / used to separate directories
dir_list = os.listdir(path) 
   
print("Files and directories in '", path, "' :")  
   
print(dir_list)