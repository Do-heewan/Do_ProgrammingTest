N, M = map(int, input().split())

now = list(map(int, input().split()))
past = list(map(int, input().split()))

ans = 0

for i in range(max(N, M)):
    a = now[i] if i < N else 0
    b = past[i] if i < M else 0
    ans = max(ans, b - a)

print(ans)