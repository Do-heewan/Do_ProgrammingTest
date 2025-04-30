# 1005 ACM Craft

import sys
input = sys.stdin.readline

T = int(input())

def get_cost(num):
    if (dp[num]) is not None:
        return dp[num]
    
    mx = 0
    for i in range(1, u+1):
        if (graph[i][num]):
            mx = max(mx, get_cost(i))

    dp[num] = mx + cost[num]

    return dp[num]

for _ in range(T):
    u, v = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    
    graph = [[False for _ in range(u+1)] for _ in range(u+1)]
    dp = [None for _ in range(u+1)]

    for _ in range(v):
        a, b = map(int, input().split())
        graph[a][b] = True
    
    target = int(input())

    print(get_cost(target))