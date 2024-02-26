import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_case = input()
camel_case = snake_to_camel(snake_case)
print(camel_case)
