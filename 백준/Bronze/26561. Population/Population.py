n = int(input())
for _ in range(n):
    p, t = map(int, input().split())
    
    born_people = t // 4
    die_people = t // 7
    
    print(p + born_people - die_people)