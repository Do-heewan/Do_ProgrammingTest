# 10813 공 바꾸기

N, M = map(int, input().split())

basket = [i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    temp = basket[a]
    basket[a] = basket[b]
    basket[b] = temp

print(*basket[1:])