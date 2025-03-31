# 1806 부분 합

N, S = map(int, input().split())
sequence = list(map(int, input().split()))

start, end = 0, 0
min_length = 100_000
sum = 0

while (True):
    if (sum >= S):
        min_length = min(min_length, end - start)
        sum -= sequence[start]
        start += 1
        
    elif (end == N):
        break
    
    else:
        sum += sequence[end]
        end += 1

print(min_length if min_length != 100_000 else 0)