# 6064 카잉 달력

T = int(input())

def find_year(m, n, x, y):
    k = x # 찾아야하는 연도

    while (k <= m*n):
        if ((k - x) % m == 0) and ((k - y) % n == 0):
            return k
        k += m
    
    return -1

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(find_year(M, N, x, y))