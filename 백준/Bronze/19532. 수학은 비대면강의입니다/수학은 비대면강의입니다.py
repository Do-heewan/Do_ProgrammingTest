# 19532 수학은 비대면강의입니다.

a, b, c, d, e, f = map(int, input().split())


x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print(int(x), int(y))