from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = [int(x) for x in input().split()]

result = multiply_list(numbers)

print(result)
