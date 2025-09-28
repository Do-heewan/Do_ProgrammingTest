N, M = map(int, input().split())

ans = 0
for _ in range(N):
    vote = input()
    
    cnt = 0
    for ix in vote:
        if ix == "O":
            cnt += 1
            
    if cnt > M / 2:
        ans += 1
        
print(ans)