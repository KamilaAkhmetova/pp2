def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input())
b = int(input())
x = squares(a, b)
for o in x:
    print(o)

        