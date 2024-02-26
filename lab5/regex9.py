import re

def insert_spaces(text):
    pattern = r'(?<!^)(?=[A-Z])'# (?<!^...) - not the start of the string, l(?=x)- to ensure that l is continued by x
    result = re.sub(pattern, ' ', text)
    return result

input_text = input()
output_text = insert_spaces(input_text)
print(output_text)
