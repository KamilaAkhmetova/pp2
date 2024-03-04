p = 1
def f(x):
    global p    
    p = p * x
    return x
l = [1,2,3,4,5]
list(map(f, l))
print(p)