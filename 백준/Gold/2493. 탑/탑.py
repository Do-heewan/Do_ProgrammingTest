# 2493 탑

N = int(input())
razer = list(map(int, input().split()))

stack = []
result = [0] * (N)

for i in range(N-1, -1, -1):
    while stack and razer[stack[-1]] < razer[i]:
        idx = stack.pop()
        result[idx] = i+1

    stack.append(i)

print(*result)