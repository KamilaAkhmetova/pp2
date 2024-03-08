start = int(input())
end = int(input())
for i in range(start, end + 1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end = " ")
