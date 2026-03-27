# 2437 저울

N = int(input())
weight = list(map(int, input().split()))
weight.sort()

target = 1
for x in weight:
    if target < x:
        break

    target += x

print(target)