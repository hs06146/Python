S = int(input())
for i in range(S):
    num, word = input().split()
    text = ''
    for i in word:
        text += int(num)*i
    print(text)