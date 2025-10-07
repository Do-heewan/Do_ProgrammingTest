N = int(input())
init = int(input())

result = 0
for _ in range(N):
    degree = int(input())
    result += min(abs(init - degree), 360-init+degree, 360+init-degree)
    init = degree

print(result)