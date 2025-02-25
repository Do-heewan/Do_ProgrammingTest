# 1931 회의실 배정

import sys
input = sys.stdin.readline

N = int(input())

time_list = []
for _ in range(N):
    start, end = map(int, input().split())
    time_list.append((start, end))

time_list.sort(key = lambda x : (x[1], x[0])) # 끝나는 시간이 빠른 순으로 정렬

target = time_list[0][1] # 가장 빨리 끝나는 회의
count = 1
for i in range(1, len(time_list)):
    if (target <= time_list[i][0]):
        target = time_list[i][1]
        count += 1

print(count)