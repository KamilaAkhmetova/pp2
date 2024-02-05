def spy_game(num_list):
    for i in range(len(num_list) - 2):
        if num_list[i] == 0 and num_list[i + 1] == 0 and num_list[i + 2] == 7:
            return True
    return False

num = input()
num_list = [int(x) for x in num.split()]
print(spy_game(num_list))
