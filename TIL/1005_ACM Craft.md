# [Gold III] ACM Craft - 1005 

[문제 링크](https://www.acmicpc.net/problem/1005) 

![ACM Craft](https://github.com/user-attachments/assets/280983b3-d316-4412-adb7-48479ed41269)


### 🗝️알고리즘 분류
- 그래프 이론
- 다이나믹 프로그래밍

---

<br>

## 💻문제 정의
건물이 순서대로 지어진다. 또한 각 건물마다 짓는데 걸리는 시간도 주어진다. 건물은 1번부터 순서대로 지어지며, 특정 건물을 가장 빨리 지을때 까지 걸리는 최소 시간을 구하는 프로그램을 작성하는 문제이다.

<Br>

## 💡접근 및 설계
문제를 보자마자 가중치가 있는 그래프의 너비 우선 탐색을 활용하려 하였다.

하지만 여러번 시도 끝에 이 문제 또한 DP로 해결하여야 하는 문제인것 같아서 DP로 접근하였다.

<br>

### ✏️알고리즘 풀이
``` python
def get_cost(num):
    if (dp[num]) is not None:
        return dp[num]
    
    mx = 0
    for i in range(1, u+1):
        if (graph[i][num]):
            mx = max(mx, get_cost(i))

    dp[num] = mx + cost[num]

    return dp[num]
```

문제의 예시를 바탕으로 설계하자면, target이 될 4번 건물을 기준으로 그래프를 역추적 하여 부모 노드에서 소요 시간이 더 큰 건물인 3번 건물의 소요시간을 더한다. 부모 노드는 재귀 함수 호출을 이용하여 소요 시간을 리턴할 수 있고, 현재의 소요 시간과 부모 노드의 건물의 소요시간을 비교하여 더 큰 값을 더하여 저장하도록 설계하였다.

<br>

```python 
u, v = map(int, input().split())
cost = [0] + list(map(int, input().split()))

graph = [[False for _ in range(u+1)] for _ in range(u+1)]
dp = [None for _ in range(u+1)]

for _ in range(v):
    a, b = map(int, input().split())
    graph[a][b] = True

target = int(input())
```

함수의 재귀 호출을 사용하다 보니 시간초과가 발생하였다. PyPy3으로 제출을 하도록 하자.

또한 이 문제를 풀면서 알게 된 사실인데, dp 리스트 초기화 부분에서, 처음에는 False로 초기화 하여 get_cost()함수에서 not dp[]를 이용하였다. 이를 어떠한 방식을 활용해도 시간초과가 발생하였는데 정답은 None에 있었다.

일반적으론 None과 False의 차이는 크게 없지만, 대규모 입력/재귀 시에는 None이 더 안정적이고 빠를 수 있다고 한다.

<br>

### 🗒️제출 코드
```python
# 1005 ACM Craft

import sys
input = sys.stdin.readline

T = int(input())

def get_cost(num):
    if (dp[num]) is not None:
        return dp[num]
    
    mx = 0
    for i in range(1, u+1):
        if (graph[i][num]):
            mx = max(mx, get_cost(i))

    dp[num] = mx + cost[num]

    return dp[num]

for _ in range(T):
    u, v = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    
    graph = [[False for _ in range(u+1)] for _ in range(u+1)]
    dp = [None for _ in range(u+1)]

    for _ in range(v):
        a, b = map(int, input().split())
        graph[a][b] = True
    
    target = int(input())

    print(get_cost(target))
```

---

### [[Python] 1005 - ACM Craft](https://do-heewan.tistory.com/156)