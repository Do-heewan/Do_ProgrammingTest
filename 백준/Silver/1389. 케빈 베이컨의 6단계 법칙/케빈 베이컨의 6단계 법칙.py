# 1389 케빈 베이컨의 6단계 법칙

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(num):
    visited = [False for _ in range(N+1)] # 방문 표시
    result = [] # 케빈 베이컨 수 저장 리스트

    visited[num] = True

    Q = deque()
    Q.append([num, 0])
    result.append([num, 0])
    
    while Q:
        c, b_num = Q.popleft()

        b_num += 1 # 노드 하나를 거침
        for ix in graph[c]:
            if not visited[ix]:
                Q.append([ix, b_num]) # 해당 노드에서 다음 노드로 거칠 때, 다음 노드와 거친 횟수를 함께 저장
                result.append([ix, b_num])
                visited[ix] = True

    return result # 리스트 형태로 반환
    
bacon_num = []
for i in range(1, N+1):
    bfs_result = bfs(i) # 각 노드 탐색 시작
    val = 0

    for j in range(len(bfs_result)):
        val += bfs_result[j][1] # 탐색후 결과 리스트를 통해 전체 bacon_num을 구함
    
    bacon_num.append(val) # 리스트에 저장

print(bacon_num.index(min(bacon_num)) + 1) # 최솟값의 인덱스 + 1 을 출력