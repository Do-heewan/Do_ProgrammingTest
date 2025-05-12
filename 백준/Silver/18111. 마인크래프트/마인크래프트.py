# 18111 마인크래프트

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

time = int(1e9)
height = 0

for h in range(257):
    use_block = 0
    get_block = 0
    for i in range(N):
        for j in range(M):
            # 블럭을 쌓아야하는 경우
            if (h > matrix[i][j]):
                use_block += h - matrix[i][j]

            # 블럭을 지워야 하는 경우
            else:
                get_block += matrix[i][j] - h

    # 사용한 블럭이 처음 블록 + 얻은 블록 수 보다 작아야 함.
    if (use_block > get_block + B):
        continue

    result = get_block * 2 + use_block

    if (result <= time):
        time = result
        height = h

print(time, height)