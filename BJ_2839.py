# N킬로그램 배달. 최대한 적은 봉지. 봉지는 3킬로그램, 5킬로그램 있음.
sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar % 5 == 0: # 입력받은 수가 5의 배수이면
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3 # 입력받은 수가 5의 배수가 아니면 3킬로그램을 빼주고 봉지+1
    bag += 1
else:
    print(-1)