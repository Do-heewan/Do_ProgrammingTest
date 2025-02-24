# 1966 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    N, M = map(int, input().split()) # N개의 출력물 / M번째가 언제 뽑히는지
    imp = list(map(int, input().split())) # 중요도 리스트 형태로 입력받기
    idx = list(i for i in range(N)) # 인덱스 번호 받기

    # 큐에 저장
    Q = deque() 
    for ix in imp:
        Q.append(ix)

    count = 0
    while M in idx:
        # 가장 앞에 가장 큰 수가 나올때 까지 pop 후 push
        while (Q[0] != max(Q)):
            Q.append(Q.popleft())
            idx.append(idx.pop(0)) # 인덱스 번호도 함께 pop & push

        # 가장 큰 수 출력 및 출력 순서 저장
        Q.popleft()
        idx.pop(0)
        count += 1
    
    print(count)