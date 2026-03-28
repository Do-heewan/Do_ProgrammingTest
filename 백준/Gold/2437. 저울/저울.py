# 2437 저울

N = int(input())
choo = list(map(int, input().split()))

choo.sort()

target = 1
for c in choo:
    if target < c:
        break

    target += c

print(target)