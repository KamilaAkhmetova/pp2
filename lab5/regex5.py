import re

txt = input()
x = bool(re.search(r"\Aa.*b\Z", txt)) 

if x:
    print("found")
else:
    print("error")
