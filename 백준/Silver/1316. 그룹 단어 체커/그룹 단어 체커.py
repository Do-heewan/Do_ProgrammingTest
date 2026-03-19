# 1316 그룹 단어 체커

N = int(input())

ans = 0
for _ in range(N):
    word = input()

    curr = ''
    lst = []
    isAble = True
    
    for w in word:
        if curr == w:
            continue
        
        if w in lst:
            isAble = False

        curr = w
        lst.append(w)

    if isAble:
        ans += 1

print(ans)