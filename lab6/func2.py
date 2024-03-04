txt = input()
num_u = 0
num_l = 0
for i in txt:
    if i.isupper():
        num_u += 1
    elif i.islower():
        num_l += 1
print(num_u)
print(num_l)
