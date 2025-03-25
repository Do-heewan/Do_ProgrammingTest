# 2467 용액

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start, end = 0, N-1

answer = abs(liquid[start] + liquid[end]) # 두 용액의 합
result = [liquid[start], liquid[end]] # 두 용액 저장 리스트

while (start < end):
    min = liquid[start] # 가장 작은 용액
    max = liquid[end] # 가장 큰 용액

    sum = min + max # 두 용액의 합

    if (abs(sum) < answer):
        answer = abs(sum)
        result = [min, max]

        if (answer == 0): # 합이 0이면 무조건 최솟값
            break

    if (sum < 0): # 합이 음수일 경우, 그 다음 작은 용액으로 변경
        start += 1

    else: # 합이 양수일 경우, 그 다음 큰 용액으로 변경
        end -= 1

print(result[0], result[1])