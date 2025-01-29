# 1920 수 찾기

import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int ,input().split())) # 정답지

M = int(input())
M_list = list(map(int ,input().split())) # 답안지

N_set = set(N_list) # 집합 변환(중복 제거)

for ix in M_list:
    if (ix in N_set):
        print(1)
    else:
        print(0)