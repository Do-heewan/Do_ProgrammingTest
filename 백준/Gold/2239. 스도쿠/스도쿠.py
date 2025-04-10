# 2239 스도쿠

matrix = [[] for _ in range(9)]

for i in range(9):
    line = input()

    for ix in line:
        matrix[i].append(int(ix))

a = [[0 for _ in range(10)] for _ in range(10)]
c = [[False for _ in range(10)] for _ in range(10)] 
c2 = [[False for _ in range(10)] for _ in range(10)]
c3 = [[False for _ in range(10)] for _ in range(10)]

def square(x, y):
    return (x//3) * 3 + (y//3)

def go(z):
    if (z == 81):
        for i in range(9):
            for j in range(9):
                print(a[i][j], end='')
            print()
        
        exit(0)
    
    x = z // 9
    y = z % 9

    if (a[x][y] != 0):
        return go(z+1)
    
    else:
        for i in range(1, 10):
            if (c[x][i] == 0) and (c2[y][i] == 0) and (c3[square(x, y)][i] == 0):
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = True

                a[x][y] = i

                if (go(z+1)):
                    return True
                
                a[x][y] = 0
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = False

    return False

for i in range(9):
    for j in range(9):
        a[i][j] = matrix[i][j]
        if (a[i][j] != 0):
            c[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[square(i, j)][a[i][j]] = True

go(0)