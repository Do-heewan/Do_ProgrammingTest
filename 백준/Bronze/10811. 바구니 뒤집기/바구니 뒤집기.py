# 10811 바구니 뒤집기

def reverse(i, j, list):
    new_list = []
    for w in range(i):
        new_list.append(list[w])
    for x in range(j, i-1, -1):
        new_list.append(list[x])
    for y in range(j+1, len(list)):
        new_list.append(list[y])

    return new_list

N, M = map(int, input().split())
bucket = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    bucket = reverse(i, j, bucket)

for ix in range(1, len(bucket)):
    print(bucket[ix], end = " ")