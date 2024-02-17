def gen(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
x = gen(n)
for a in x:
    print(a)
