# 7453 합이 0인 네 정수

N = int(input())

a, b, c, d = [], [], [], []
for _ in range(N):
    a1, b1, c1, d1 = map(int, input().split())
    a.append(a1)
    b.append(b1)
    c.append(c1)
    d.append(d1)

dic = {}

for ax in a:
    for bx in b:
        if ax+bx in dic:
            dic[ax+bx] += 1
        else:
            dic[ax+bx] = 1

answer = 0
for cx in c:
    for dx in d:
        if -cx-dx in dic:
            answer += dic[-cx-dx]

print(answer)