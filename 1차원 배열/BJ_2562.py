num = 0
index = 0

for i in range(9):
    a = int(input())

    if(a > num):
        num = a
        index = i + 1
print('%d\n%d'%(num, index))