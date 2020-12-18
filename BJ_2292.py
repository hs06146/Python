#규칙 : 지나가는 방의 개수가 1씩 증가할수록 숫자는 6개씩 증가한다.
num = int(input())
first = 1
room = 6
count = 1
while num > first:
    count += 1
    first += room
    room += 6
print(count)
