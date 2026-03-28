# 13164 행복 유치원

N, K = map(int, input().split())
group = list(map(int, input().split()))

diff = []
for i in range(N-1):
    diff.append(group[i+1]-group[i])

diff.sort()

print(sum(diff[:N-K]))