import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

for i in range(N):
    for j in range(M):
        if ((i*M + j) == K):
            print(i, j)
