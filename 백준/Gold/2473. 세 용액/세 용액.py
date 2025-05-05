# 2473 세 용액

import sys

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

answer = sys.maxsize

for i in range(N-2):
    start = i+1
    end = N-1

    while (start < end):
        fix = liquid[i] # 용액 고정
        min = liquid[start] # 고정 용액을 제외한 가장 작은 용액
        max = liquid[end] # 고정 용액을 제외한 가장 큰 용액

        sum = fix + min + max # 용액 합

        if (abs(sum) < answer):
            answer = abs(sum)
            result = [liquid[i], min, max]

        if (sum < 0): # 합이 음수일 경우, 그 다음 작은 용액으로 변경
            start += 1

        elif (sum > 0): # 합이 양수일 경우, 그 다음 큰 용액으로 변경
            end -= 1
        
        else: # 합이 0일 경우, 가장 작은 경우
            break

for ix in result:
    print(ix, end = ' ')