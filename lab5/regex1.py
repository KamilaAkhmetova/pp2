import re
def s(a,b):
    return bool(re.search(a,b))
a=r"ab+" # + - from 1 to inf
t = ["a", "ab", "abb", "abbb", "ac", "bc", "b"]
for b in t:
    if s(a,b):
        print(f"'{b}'found")
    else:
        print("error")