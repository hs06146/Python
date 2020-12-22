#규칙 : 지나가는 방의 개수가 1씩 증가할수록 숫자는 6개씩 증가한다.
num = int(input())
first = 1
room = 6
count = 1
#입력 받은 값이 이전 방보다 클 경우
while num > first:
    count += 1
    first += room
    room += 6
print(count)
