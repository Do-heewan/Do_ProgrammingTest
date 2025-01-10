# 2630 색종이 만들기

N = int(input())

mat = []
for _ in range(N):
    element = list(map(int, input().split()))
    mat.append(element)

blue = 0
white = 0

def check(x, y, n):
    global blue
    global white
    ch = mat[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):

            if (ch != mat[i][j]):
                check(x, y, n//2)
                check(x + n//2, y, n//2)
                check(x, y + n//2, n//2)
                check(x + n//2, y + n//2, n//2)
                return
            
    if (ch == 1):
        blue += 1
    else:
        white += 1

check(0, 0, N)
print(white)
print(blue)