# 34323 할인이 필요해

N, M, S = map(int, input().split())

discount = S * (100 - N) * (M + 1) // 100
print(min(discount, S * M))