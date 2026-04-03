# 2096 내려가기

N = int(input())

prev_max = [0, 0, 0]
prev_min = [0, 0, 0]

for i in range(N):
    a, b, c = map(int, input().split())
    curr_max = [0, 0, 0]
    curr_min = [0, 0, 0]

    curr_max[0] = max(prev_max[0], prev_max[1]) + a
    curr_max[1] = max(prev_max[0], prev_max[1], prev_max[2]) + b
    curr_max[2] = max(prev_max[1], prev_max[2]) + c

    curr_min[0] = min(prev_min[0], prev_min[1]) + a
    curr_min[1] = min(prev_min[0], prev_min[1], prev_min[2]) + b
    curr_min[2] = min(prev_min[1], prev_min[2]) + c

    prev_max = curr_max
    prev_min = curr_min

print(max(prev_max), min(prev_min))