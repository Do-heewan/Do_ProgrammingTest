import sys
from collections import Counter

# 입력 받기
N = int(sys.stdin.readline().strip())
N_li = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
M_li = list(map(int, sys.stdin.readline().split()))

# N_li에 있는 숫자의 개수를 미리 세기
count_dict = Counter(N_li)

# M_li의 각 원소에 대해 개수 출력
print(" ".join(str(count_dict[m]) if m in count_dict else "0" for m in M_li))
