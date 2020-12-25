N = new = int(input())
count = 0
while True:
    ten = N//10
    one = N%10
    result = ten+one
    count+=1
    N = int(str(N%10)+str(result%10))

    if(new == N):
        break
print(count)