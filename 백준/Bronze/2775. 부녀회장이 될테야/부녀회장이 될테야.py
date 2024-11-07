T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    
    floor_0 = [x for x in range(1, n+1)]
    for j in range(k):
        floor = []
        for k in range(n):
            floor.append(sum(floor_0[:k+1]))
        floor_0 = floor.copy()
    print(floor[-1])