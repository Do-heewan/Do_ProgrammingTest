# 1834 나머지와 몫이 같은 수

N = int(input())

INF = 2_000_000

res = []
for i in range(1, N):
    res.append(N*i + i)

print(sum(res))