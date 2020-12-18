X = int(input())
line = 1
while X>line:
    X -= line
    line += 1
#짝수 라인과 홀수 라인 구분
if line%2 == 0:
    a = X
    b = line-X+1
else:
    a = line-X+1
    b = X

print(a, '/', b, sep='')