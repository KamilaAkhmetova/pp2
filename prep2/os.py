import os

print(dir(os)) #it returns the names of all attributes and methods available within the os module.

print(os.getcwd()) # print the current working directory.

os.chdir(r"C:\Users\Kamila\Desktop\kbtu\pp2\lab6")
print(os.getcwd()) #os.chdir(path): This function changes the current working directory to the one specified by path.

print(os.listdir()) #a list of all the entries (files, directories, etc.) in the specified directory. If no directory path is specified, it defaults to the current working directory.

os.chdir(r"C:\Users\Kamila\Desktop\kbtu\pp2\prep2")

#os.makedirs("OS-Demo-2\Sub-Dir-1") #creates
#print(os.listdir())

#os.rmdir("OS-Demo-2\Sub-Dir-1")  removes

#os.rename('a.txt', 'b.txt') # changes names (os.rename('original', 'new'))

print(os.stat('b.txt')) # the information about b.txt

print(os.stat('b.txt').st_size) # prints only size

for dirpath, dirnames, filenames in os.walk(r"C:\Users\Kamila\Desktop\kbtu\pp2\prep2"):
    print(dirpath)
    print(dirnames)
    print(filenames)

print(os.environ.get('PATH'))
