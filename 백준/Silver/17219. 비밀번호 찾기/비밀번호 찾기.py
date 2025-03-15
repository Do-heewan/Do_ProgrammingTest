N, M = map(int, input().split())

hash = {}
for _ in range(N):
    site, pw = input().split()
    hash[site] = pw

for _ in range(M):
    print(hash[input()])