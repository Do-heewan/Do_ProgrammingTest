# 3273 두 수의 합

N = int(input())
lst = list(map(int, input().split()))
target = int(input())

lst.sort()

start = 0
end = N-1
answer = []

temp = 0
while start < end:
    temp = lst[start] + lst[end]

    if temp == target:
        answer.append([start, end])
        start += 1
        end -= 1

    elif temp > target:
        end -= 1
    
    else:
        start += 1

print(len(answer))