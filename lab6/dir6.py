import os

def generate_files():
    try:
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            file_name = letter + ".txt"
            with open(file_name, 'w') as file:
                file.write("This is file %s." % file_name)
    except Exception as e:
        print("An error occurred:", str(e))

generate_files()
print("Text files A.txt to Z.txt have been generated.")
