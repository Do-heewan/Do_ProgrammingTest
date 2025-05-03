# 위상 정렬(Topology Sort)

### 위상 정렬이란?
![위상정렬](https://github.com/user-attachments/assets/c8379e21-09e1-4822-8912-e28ae726a976)

- 정렬 알고리즘의 하나로, **순서가 정해져 있는 작업을 차례로 수행**해야할 때 사용할 수 있는 알고리즘이다.
- 방향이 있는 그래프의 노드들을 간선의 방향을 거스르지 않도록 나열하는 것

<br>

## 진입 차수와 진출 차수

위상 정렬 알고리즘을 알아보기 위해 먼저 진입 차수와 진출 차수에 대한 개념을 알아야 한다.

- 진입 차수 (Indegree) : 특정한 노드로 들어오는 간선의 개수
- 진출 차수 (Outdegree) : 특정한 노드에서 나가는 간선의 개수

<br>

## 위상 정렬 알고리즘 동작 과정

    1. 진입 차수가 0인 노드를 큐에 넣는다.
    2. 큐가 빌 때 까지 다음의 과정을 반복한다.
        a. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
        b. 진입 차수가 0이 된 노드를 큐에 새롭게 삽입

즉, 각 노드가 큐에 들어온 순서가 위상 정렬의 결과이다.

<br>

## 위상 정렬의 특징
- 위상 정렬은 **사이클이 없는 방향 그래프 (DAG, Direct Acyclic Graph)**에 대해서만 수행할 수 있다.
- 위상 정렬에는 여러 개의 결과가 존재할 수 있다. 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면 여러 개의 결과가 존재한다는 의미이다.
- 모든 원소를 방문하기 전에 큐가 비게 된다면 사이클이 존재한다는 의미이다.
- 보통 큐로 구현하나, 스택으로도 구현할 수 있다.

<br>

## 위상 정렬 함수 구현 (Python)
```python
from collections import deque

# 노드와 간선의 개수 입력
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
```

### 시간 복잡도
- `O(V+E)`
- 차례대로 모든 노드를 확인`O(V)`, 해당 노드에서 출발하는 간선을 차례대로 제거`O(E)`이다. 