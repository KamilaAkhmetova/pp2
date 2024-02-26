import re

def s(pattern, text):
    return bool(re.search(pattern, text))

pattern = r"^[A-Z]+[a-z]$"
texts = ["a", "ab", "abbC", "Ac", "AAA_ooo", "a_"]

for text in texts:
    if s(pattern, text):
        print(f"'{text}' matches")
    else:
        print(f"'{text}' does not match")
