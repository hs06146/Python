arr = []
for i in range(10):
    A = int(input())
    arr.append(A%42)
arr = set(arr)
print(len(arr))