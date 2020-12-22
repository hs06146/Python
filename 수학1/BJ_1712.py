# A, B, C가 빈 칸을 사이에 두고 순서대로 주어짐. 자연수.
# A: 고정비용, B: 가변비용, C: 노트북 가격
A, B, C = map(int, input().split())
# 손익분기점이 존재하지 않으면 -1 출력
if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+1))

