# 27172 수 나누기 게임

def eratostenes(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
    return True

N = int(input())
x = list(map(int, input().split()))
pos = [-1] * 1_000_001

for i in x:
    pos[i] = i

score = [0] * 1_000_001
for i in range(N):
    curr = x[i]

    for c in range(curr * 2, 1_000_001, curr):
        if pos[c] != -1:
            score[curr] += 1
            score[c] -= 1

for i in range(N):
    print(score[x[i]], end=" ")