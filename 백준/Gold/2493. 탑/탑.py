# 2493 탑

N = int(input())
nums = list(map(int, input().split()))

stack = []
result = [0] * N
for i in range(N):
    while stack:
        if nums[stack[-1]] > nums[i]:
            result[i] = stack[-1]+1
            break
        else:
            stack.pop()

    stack.append(i)

print(*result)