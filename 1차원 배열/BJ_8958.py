a = int(input())
for i in range(a):
    ox = input()
    result = list(ox)
    sum = 0
    count = 1
    for i in result:
        if i == 'O':
            sum += count
            count += 1
        else :
            count = 1
    print(sum)