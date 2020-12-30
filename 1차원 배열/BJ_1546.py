N = int(input())
score = list(map(int, input().split()))
max = 0
avg = 0

for i in range(N):
    if max < score[i]:
        max = score[i]

for i in range(N):
    score[i] = score[i]/max * 100.0
    avg += score[i]

print(round(avg/N, 2))