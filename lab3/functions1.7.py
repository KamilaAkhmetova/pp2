def has_33(numbers_list):
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] == 3 and numbers_list[i + 1] == 3:
            print("True")
            return True
    print("False")
    return False

input_numbers = input("Input: ")
numbers_list = [int(x) for x in input_numbers.split()]
has_33(numbers_list)
