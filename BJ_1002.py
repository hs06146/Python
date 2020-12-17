T = int(input()) # Number of test case
for i in range(T):
    """
    Test Case
    x1, y1, x2, y2 >= -10000
    x1, y1, x2, y2, r1, r2 <= 10000
    x,y = Center of circle
    r = radius
    """
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
    rSum = r1 + r2  #radius + radius
    rm = abs(r1 - r2) # radius - radius
    """
    Two circles overlap each other,
    Have infinite point
    """
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == rSum or d == rm:
            print(1)
        elif rSum > d > rm:
            print(2)
        else:
            print(0)
