# 10816 숫자 카드 2

from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

count = Counter(N_list)
print(" ".join(str(count[i]) if i in count else "0" for i in M_list))