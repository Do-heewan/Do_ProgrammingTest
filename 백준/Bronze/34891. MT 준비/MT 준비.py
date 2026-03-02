# 34891 MT 준비

N, M = map(int, input().split())

cnt = N // M

print(cnt if N % M == 0 else cnt + 1)