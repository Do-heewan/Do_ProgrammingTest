import bisect

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A_sum = []
for i in range(N):
    s = 0
    for j in range(i, N):
        s += A[j]
        A_sum.append(s)

B_sum = []
for i in range(M):
    s = 0
    for j in range(i, M):
        s += B[j]
        B_sum.append(s)

B_sum.sort()

ans = 0
for a in A_sum:
    target = T - a
    left = bisect.bisect_left(B_sum, target)
    right = bisect.bisect_right(B_sum, target)
    ans += (right - left)

print(ans)