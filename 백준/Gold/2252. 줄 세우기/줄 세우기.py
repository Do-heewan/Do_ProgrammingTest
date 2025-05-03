# 2252 줄 세우기

from collections import deque

N, M = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (N + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    Q = deque()

    for i in range(1, N+1):
        if (indegree[i] == 0):
            Q.append(i)

    while Q:
        now = Q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for g in graph[now]:
            indegree[g] -= 1
            if (indegree[g] == 0):
                Q.append(g)

    # 위상 정렬 수행한 결과 출력
    for res in result:
        print(res, end=' ')

topology_sort()