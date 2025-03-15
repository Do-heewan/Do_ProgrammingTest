# 11047 동전 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))

def cash(num):
    count = []
    idx = len(coin)-1
    target = coin[idx]

    while (num != 0):
        if (target > num): # 가장 큰 값의 동전이 현재 가격보다 크다면
            idx -= 1
            target = coin[idx]

        else:
            count.append(num // target)
            num -= count[-1] * target

    return sum(count)

print(cash(K))