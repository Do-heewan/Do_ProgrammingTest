# 8980 택배

N, C = map(int, input().split())
M = int(input())

truck = []
for _ in range(M):
    truck.append(list(map(int, input().split())))

truck.sort(key=lambda x : (x[1]))

load = [0] * (N+1)
total_cost = 0

for a, b, cost in truck:
    max_load = max(load[a:b]) 

    possible = min(cost, C-max_load)

    for i in range(a, b):
        load[i] += possible

    total_cost += possible

print(total_cost)