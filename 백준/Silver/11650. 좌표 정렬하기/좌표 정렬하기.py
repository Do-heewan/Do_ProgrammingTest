# 11650 좌표 정렬하기

n = int(input())

li = []
for i in range(n):
    [h, w] = input().split()
    li.append([h, w])

li.sort(key = lambda x : (int(x[0]), int(x[1])))

for j in li:
    print(j[0], j[1])