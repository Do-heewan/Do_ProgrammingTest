A = []
B = []

N, M = map(int, input().split())

for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(N):
    for j in range(M):
        sum = A[i][j] + B[i][j]
        print(sum, end = ' ')
    print()