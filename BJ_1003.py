T = int(input())

def count_fibo(T):
    zero = [1,0]
    one = [0,1]
    if T <= 1:
        return
    for i in range(2, T+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])

    return zero, one

zero, one = count_fibo(40)

for j in range(T):
    n = int(input())
    print("%d %d" %(zero[n], one[n]))
