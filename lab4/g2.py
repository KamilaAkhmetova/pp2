def gen(n):
    for  i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
x = gen(n)
for a in x:
    print(a, end = ", ")