# 1009 분산처리

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    ans = pow(a, b, 10)
    print(ans if ans != 0 else 10)