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
    max_count = max(count.values())
    result = [k for k, v in count.items() if (v == max_count)]

    if (len(result) < 2):
        return result[0]

    return sorted(result)[1]

# 범위
def num_range(list):
    return (max(list) - min(list))

print(mean(seq))
print(mid(seq))
print(freq(seq))
print(num_range(seq))