def fibonacci(n):
    if n <= 2:
        yield 1
    else:
        a, b = 1, 1
        yield a
        yield b
        for _ in range(2, n):
            a, b = b, a + b
            yield b

a = int(input())
fib_sequence = list(fibonacci(a))
print(fib_sequence)
