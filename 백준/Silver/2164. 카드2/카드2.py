# 2164 카드2

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

Q = deque() # 큐 생성
for i in range(1, N+1):
    Q.append(i) # 1 부터 N까지 추가

while (len(Q) > 1): # Q에 카드 한 장 남을때 까지
    Q.popleft() # 최상단 제거
    Q.append(Q.popleft()) # 두번째 카드 뒤로 옮기기 (제거와 동시에 맨 뒤에 추가)

print(*Q) # Q 내부 원소만 출력