# 1932 정수 삼각형

N = int(input())

tri = []
for _ in range(N):
    num_list = list(map(int, input().split()))
    tri.append(num_list)

for i in range(1, N):
    for j in range(len(tri[i])):
        if (j == 0):
            tri[i][j] += tri[i-1][j]

        elif (j == len(tri[i])-1):
            tri[i][j] += tri[i-1][j-1]

        else:
            tri[i][j] = max(tri[i][j] + tri[i-1][j-1], tri[i][j] + tri[i-1][j])

print(max(tri[N-1]))