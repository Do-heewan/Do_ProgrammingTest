# 17219 비밀번호 찾기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

hash = {}
for _ in range(N):
    site, pw = input().split()
    hash[site] = pw

for _ in range(M):
    print(hash[input().rstrip()])