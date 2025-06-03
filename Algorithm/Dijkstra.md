# 다익스트라(Dijkstra) 알고리즘

### 다익스트라 알고리즘이란?

그래프의 한 정점에서 모든 정점까지의 최단 거리를 각각 구하는 알고리즘(최단 경로 문제, Short Path Problem)이다.

간선의 가중치가 음수인 경우에는 사용하지 못한다.

<br>

### 다익스트라 알고리즘 동작 과정

    1. 각 정점과 정정 간의 가중치 정보 입력
    2. 시작 정점에서 부터 시작하여 방문하지 않은 인접 노드들 방문
    3. 현재의 가중치 + 다음 정점으로 가는데 드는 비용과 다음 정점의 현재 가중치를 비교하여 더 작은 값을 넣어준다.
    4. 모든 정점을 방문할 때 까지 반복한다.

파이썬에서는 가중치에 대해 min-heap으로 정렬할 수 있도록 우선순위 큐를 활용한다.

<br>

### 다익스트라 알고리즘 구현 (Python)

``` python
import heapq

graph = [[] for _ in range(V+1)] 
weight = [INF] * (V+1) # 가중치 합 저장 리스트

def dijkstra(num):
    queue = []
    heapq.heappush(queue, (0, num)) # 시작 위치의 가중치는 0
    weight[num] = 0

    while queue:
        wgt, now = heapq.heappop(queue) # 큐에 저장된 가중치와 정점 정보 pop

        if (weight[now] < wgt): # 현재 정점에 저장된 가중치가 더 작다 => 이미 작은 가중치로 현재 정점에 도착함
            continue

        for v, w in graph[now]:
            cost = wgt + w # 비용 = v로 가는데 드는 가중치 + 현재의 가중치
            if (cost < weight[v]): # 비용이 더 적게 들면
                weight[v] = cost # 더 작은 가중치로 변경
                heapq.heappush(queue, (cost, v)) # 힙에 푸쉬
```

