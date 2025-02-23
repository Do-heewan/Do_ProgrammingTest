# 1929 소수 구하기

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N+1):
    if (i == 1): # 1 부터 시작인 경우, 1은 제외
        continue

    for j in range(2, int(i ** 0.5) + 1): # 2 ~ 제곱근 사이의 수만 비교
        if (i % j == 0): # 나누어 떨어질 경우 소수 X
            break # break를 만날경우, else 실행 X

    else: # for문을 통과 후 i 출력
        print(i)