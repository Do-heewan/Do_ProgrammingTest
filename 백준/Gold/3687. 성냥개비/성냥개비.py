# 3687 성냥개비

def makeMin(num):
    INF = 1_000_000_000_000_000

    minNum = [INF] * 101
    minNum[2] = 1
    minNum[3] = 7
    minNum[4] = 4
    minNum[5] = 2 # [2, 3, 5]
    minNum[6] = 6 # [0, 6, 9]
    minNum[7] = 8

    arr = [INF, INF, 1, 7, 5, 2, 0, 8] # 각 개수마다 만들수 있는 가장 작은 수
    for i in range(8, 101):
        for j in range(2, 8): # 0개, 1개는 존재하지 않으므로, 2~8개로 만들 수 있는 수를 붙였을 때, 현재 수보다 큰지 판별
            minNum[i] = min(minNum[i], int(str(minNum[i-j]) + str(arr[j])))

    return minNum[num]


def makeMax(num):
    maxNum = [0] * 101
    maxNum[2] = 1
    maxNum[3] = 7

    arr = [0, 0, 1, 7]
    for i in range(4, 101):
        for j in range(2, 4):
            maxNum[i] = max(maxNum[i], int(str(maxNum[i-j]) + str(arr[j])))

    return maxNum[num]

T = int(input())
for _ in range(T):
    num = int(input())
    print(makeMin(num), makeMax(num))
