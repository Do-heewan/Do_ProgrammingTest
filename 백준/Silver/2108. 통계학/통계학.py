# 2108 통계학

from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())

seq = []
for _ in range(N):
    num = int(input())
    seq.append(num)

# 산술평균
def mean(list):
    return round(sum(list) / len(list))

# 중앙값
def mid(list):
    list.sort()
    return list[len(list) // 2]

# 최빈값
def freq(list):
    count = Counter(list) # 항목별 개수 카운팅 후 딕셔너리 형태로 저장
    max_count = max(count.values()) # 카운팅 개수의 최댓값
    result = [k for k, v in count.items() if (v == max_count)] # (원소, 개수)의 형태에서, 개수가 max_count일 때, 해당 원소만 리스트에 저장

    if (len(result) < 2): # 길이가 2보다 작으면 첫번째 출력
        return result[0]

    return sorted(result)[1] # 정렬 후, 2번째 원소 출력

# 범위
def num_range(list):
    return (max(list) - min(list))

print(mean(seq))
print(mid(seq))
print(freq(seq))
print(num_range(seq))