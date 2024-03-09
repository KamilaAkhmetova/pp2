f = open('text.txt', 'r')
print(f.name)
f.close()

f = open('text.txt', 'r')
print(f.mode)
f.close()

with open('text.txt', 'r') as f:
    pass
print(f.closed)

with open('text.txt', 'r') as f:
    print(f.read())

with open('text.txt', 'r') as f:
    f_contents = f.read()
print(f_contents)

with open('text.txt', 'r') as f:
    f_contents = f.readlines()
print(f_contents)

with open('text.txt', 'w') as f:
    f.write('how are you')
with open('text.txt', 'r') as f:
    print(f.read())
    