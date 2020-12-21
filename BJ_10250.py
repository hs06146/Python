T = int(input())

for i in range (T):
    H, W, N = map(int, input().split())
    room_num = N//H+1 #방 호수
    floor = N % H #층 수
    if floor == 0: #H의 배수이면
        room_num = N//H
        floor = H
    print(floor*100+room_num)