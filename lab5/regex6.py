import re
txt = input()
x = re.sub(r"\s|,|\.", ":", txt)
print(x)