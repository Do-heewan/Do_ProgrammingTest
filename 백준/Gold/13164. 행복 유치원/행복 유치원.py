# 13164 행복 유치원

N, K = map(int, input().split())
cost = list(map(int, input().split()))

diff = []
for i in range(N-1):
    diff.append(cost[i+1]-cost[i])

diff.sort(reverse=True)

print(sum(diff[K-1:]))