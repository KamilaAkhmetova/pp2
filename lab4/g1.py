def gen(N):
    for i in range(1, N):
        yield i**2
    
N=int(input())
x=gen(N)
for a in x:
    if a<=N:
        print(a)