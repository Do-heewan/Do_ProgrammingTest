T = int(input())

for i in range(T):
    C = int(input())
    cost = [25, 10, 5, 1]
    result = [0] * 4
    
    while C > 0:
        if C >= cost[0]:
            C -= cost[0]
            result[0] += 1
        elif C >= cost[1]:
            C -= cost[1]
            result[1] += 1
        elif C >= cost[2]:
            C -= cost[2]
            result[2] += 1
        else:
            C -= cost[3]
            result[3] += 1
    
    for ix in result:
        print(ix, end = " ")
    print()