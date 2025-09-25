# 11054 가징 긴 바이토닉 부분 수열

N = int(input())
lst = list(map(int, input().split()))
rev_lst = lst[::-1]

dpMax = [1] * N
dpMin = [1] * N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dpMax[i] = max(dpMax[i], dpMax[j]+1)
        
        if rev_lst[i] > rev_lst[j]:
            dpMin[i] = max(dpMin[i], dpMin[j]+1)

dpMin = dpMin[::-1]

result = []
for i in range(N):
    result.append(dpMax[i] + dpMin[i])

print(max(result) - 1)