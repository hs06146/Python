def d(n):
    next = n
    for value in list(str(n)):
        next += int(value)
    return next

ex = []

for count in range(10001):
    ex.append(d(count))

for count in range(1,10000):
    if count in ex:
        continue
    else:
        print(count)