# 9663 N-Queen

N = int(input())

count = 0
row = [0 for _ in range(N)]

def check(x):
    for i in range(x):
        if (row[i] == row[x]) or (abs(row[x] - row[i]) == abs(x - i)):
            return False
        
    return True

def nQueen(k):
    global count

    if (k == N):
        count += 1
        return
    
    else:
        for i in range(N):
            # [k, i]에 퀸을 놓음
            row[k] = i
            if check(k):
                nQueen(k+1)

nQueen(0)
print(count)