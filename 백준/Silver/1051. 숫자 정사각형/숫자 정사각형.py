# 1051 숫자 정사각형형

N, M = map(int ,input().split())

# 매트릭스 생성
mat = [[] for _ in range(N)]
for i in range(N):
    word = input()

    for ix in word:
        mat[i].append(ix)

def search(num):
    for i in range(N-num + 1):
        for j in range(M-num + 1):
            if (mat[i][j] == mat[i][j+num-1]) and (mat[i][j] == mat[i+num-1][j]) and (mat[i][j] == mat[i+num-1][j+num-1]):
                return True
            
    return False

size = min(N, M)

for i in range(size, 0, -1):
    if (search(i)):
        print(i ** 2)
        
        break