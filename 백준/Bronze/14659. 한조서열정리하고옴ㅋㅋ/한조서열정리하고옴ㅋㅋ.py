# 14659 한조서열정리하고옴ㅋㅋ

N = int(input())
bong = list(map(int, input().split()))

max_height = 0
cnt = 0
max_cnt = 0
for i in bong:
    if i > max_height:
        max_height = i
        max_cnt = max(cnt, max_cnt)
        cnt = 0

    else:
        cnt += 1

max_cnt = max(cnt, max_cnt)
print(max_cnt)