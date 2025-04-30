def get_cost(b):
    if dp[b] is not None:
        return dp[b]
    mx = 0
    for i in range(num_buildings):
        if need[i][b]:
            mx = max(mx, get_cost(i))
    dp[b] = mx + cost[b]
    return dp[b]

num_tests = int(input())
for _ in range(num_tests):
    num_buildings, num_rules = map(int, input().split())
    cost = list(map(int, input().split()))
    need = [ [False] * num_buildings for _ in range(num_buildings) ]
    dp = [None] * num_buildings
    # need[x][y]: must build x to build y
    for _ in range(num_rules):
        x, y = map(int, input().split())
        need[x-1][y-1] = True
    target_building = int(input()) - 1
    print(get_cost(target_building))
