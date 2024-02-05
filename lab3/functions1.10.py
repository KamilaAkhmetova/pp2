def to_unique(num_list):
    new_list = []
    for i in range(len(num_list)):
        is_unique = True
        for j in range(i + 1, len(num_list)):
            if num_list[i] == num_list[j]:
                is_unique = False
                break
        if is_unique:
            new_list.append(num_list[i])
    
    print(new_list)

num = input()
num_list = num.split()
to_unique(num_list)
