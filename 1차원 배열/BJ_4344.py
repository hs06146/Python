C = int(input())
for i in range(C):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]
    count = 0
    for j in score[1:]:
        if j > avg :
            count += 1
    print(f'{count/score[0]*100:.3f}%')

