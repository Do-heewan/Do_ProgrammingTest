# 벨만-포드(Bellman-Ford) 알고리즘

### 벨만-포드 알고리즘이란?

그래프의 한 정점에서 모든 정점까지의 최단 거리를 각각 구하는 알고리즘(최단 경로 문제, Short Path Problem)이다.

음수 가중치 에지가 있어도 수행할 수 있다.

<br>

### 다익스트라 알고리즘 vs 벨만-포드 알고리즘

|Dijkstra|Bellman-Ford|
|----|-----|
|매번 방문하지 않은 노드들에 대해서 최단 거리가 짧은 정점을 선택한다.|매번 한 정점에서의 모든 간선을 확인한다.|
|음수 간선이 존재한다면 동작하지 못한다.|음수 간선이 존재하여도 동작한다.|

<br>

### 벨만-포드 알고리즘 동작 과정

    1. 시작 노드 거리 초기화
    2. 전체 노드를 방문하며 다음을 반복한다.
        2-1. 정점마다 모든 간선을 확인
        2-2. 다음 정점으로 가는 비용과 현재 정점까지의 비용 + 간선의 가중치를 비교
        2-3. 더 작은값으로 업데이트한다.
        2-4. 모든 정점에 대해서 방문을 마쳤을 때, 거리 테이블 값이 갱신된다면 음수 사이클이 존재

<br>

### 벨만-포드 알고리즘 구현 (Python)

```python
def bellman_ford(start):
    # 시작 노드 거리 초기화
    distance[start] = 0
    # 전체 노드 반복
    for i in range(N):
        # 매 반복마다 모든 간선 확인
        for j in range(2*M+W):
            curr_node = edge[j][0]
            next_node = edge[j][1]
            edge_cost = edge[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
            if (distance[next_node] > distance[curr_node] + edge_cost):
                distance[next_node] = distance[curr_node] + edge_cost

                # N-1 번째에서 값이 갱신된다면 음수 순환이 존재
                if (i == N - 1):
                    return True

    return False
```