def to_histogram(num_list):
    for value in num_list:
        print("*" * value)

num = input()
num_list = [int(x) for x in num.split()]
to_histogram(num_list)
