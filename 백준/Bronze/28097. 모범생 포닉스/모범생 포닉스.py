N = int(input())
li = list(map(int, input().split()))

sum_li = sum(li) + 8 * (N-1)

print(sum_li // 24, sum_li % 24)