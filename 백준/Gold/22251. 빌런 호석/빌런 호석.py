# 22251 빌런 호석

def convert_num(n):
    s_n = str(n)
    return list('0'*(K-len(s_n))+s_n)

N, K, P, X = map(int, input().split()) # 수의 범위, 자릿수, 바꿀 디스플레이 최대 개수, 현재 층 수

bit = [0 for _ in range(10)]
bit[0] = 0b1111101
bit[1] = 0b0101000
bit[2] = 0b0110111
bit[3] = 0b0101111
bit[4] = 0b1101010
bit[5] = 0b1001111
bit[6] = 0b1011111
bit[7] = 0b0101100
bit[8] = 0b1111111
bit[9] = 0b1101111

diff = [[0] * (10) for _ in range(10)]
for i in range(10):
    for j in range(10):
        diff[i][j] = (bit[i] ^ bit[j]).bit_count()

curr = convert_num(X)

answer = 0
for i in range(1, N+1):
    if i == X:
        continue

    next = convert_num(i)

    cnt = 0
    for j in range(K):
        cnt += diff[int(curr[j])][int(next[j])]

    if cnt <= P:
        answer += 1

print(answer)