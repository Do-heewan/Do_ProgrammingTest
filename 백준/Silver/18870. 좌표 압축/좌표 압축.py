# 18870 좌표 압축

N = int(input())
li = list(map(int, input().split()))
s_li = list(set(li))
s_li.sort()

idx_li = [i for i in range(len(s_li))]

li_dict = {key : value for key, value in zip(s_li, idx_li)}

for ix in li:
    print(li_dict[ix], end = " ")