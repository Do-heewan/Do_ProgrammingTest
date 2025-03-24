# 2166 다각형의 면적

N = int(input())

x_s = []
y_s = []
for _ in range(N):
    x, y = map(int, input().split())
    x_s.append(x)
    y_s.append(y)

x_s.append(x_s[0])
y_s.append(y_s[0])

# 신발끈 공식
area = 0
for i in range(len(x_s) - 1):
    area += x_s[i] * y_s[i+1]
    area -= x_s[i+1] * y_s[i]

print(round(abs(area) / 2, 1))