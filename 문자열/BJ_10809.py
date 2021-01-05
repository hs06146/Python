S = input()
alphabet = list(range(97, 123)) #소문자 알파벳 아스키코드 범위
for i in alphabet:
    print(S.find(chr(i)))