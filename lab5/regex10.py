import re

def camel_to_snake(text):
    pattern = r'(?<!^)(?=[A-Z])'  
    result = re.sub(pattern, '_', text)  
    snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', result).lower() 
    return snake_case

input_text = input()
output_text = camel_to_snake(input_text)
print(output_text)
