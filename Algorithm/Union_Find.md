# Disjoint Set (분리 집합)

### 분리 집합이란?
- 두 개 이상의 집합이 존재할 때, 해당 집합들이 서로소 관계에 있을 때 분리 집합이라 한다.
- 분리 집합은 하나의 자료 구조로써, 상호 배타적으로 이루어진 집합을 효율적으로 표현하기 위해 만들어졌다.
- Make_Set, Find, Union 연산 방식이 있으며, 해당 연산 방식을 따와 Union-Find 알고리즘이라고도 한다.

<br>

## Union-Find
분리 집합은 효율적인 연산을 위해 트리 구조로 구성된다.

### Find 연산
- 특정 노드로부터 재귀적으로 트리를 거슬러 올라가 루트(root) 값을 반환한다.
- 하나의 트리는 반드시 하나의 루트를 가지게 된다. 따라서 반환된 루트의 값으로 해당 노드가 어떤 집합에 속해있는지를 판별할 수 있다.

### Union 연산
- 두 노드가 속한 트리를 병합한다. Find 연산을 통해 두 노드의 루트 노드를 얻고, 한 트리의 루트를 다른 하나의 루트로 바꾸어 트리를 병합시킨다.
- 일반적으로 두 트리의 높이(rank)를 비교하여 높이가 더 낮은 트리를 높은 트리에 병합시키도록 한다.

### 경로 압축
- 1 -> 2 -> 3 -> 4 -> 5 로 이루어진 트리가 있다고 가정했을 때, 노드 5의 루트를 구하기 위해선 5 -> 4 -> 3 -> 2 -> 1 순서로 연산이 이루어 질 것이다. 이는 매우 비효율적이다.
- parent[x] = find_root(parent[x]) 적용
    - parent[5] = find_root(parent[5]) # => 4 -> find_root(parent[4]) = 3 -> ... 1
    - 즉 parent[5]에는 1이 저장됨.
<br>

## Union-Find 구현

```python
parent = [i for i in range(N+1)]

def find_root(x):
    if (parent[x] == x): return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union_set(a, b):
    x = find_root(a)
    y = find_root(b)
    if (x > y):
        parent[x] = y 
    else: 
        parent[y] = x

def same_root(a, b):
    return find_root(a) == find_root(b)
```

`find_root(x)` : x의 루트(root) 노드를 구한다.

`union_set(a, b)` : a, b 두 노드가 속한 트리를 병합 (두 노드가 속한 트리의 루트를 비교하여 트리 병합)

`same_root(a, b)` : a, b 두 노드의 루트가 같은지를 판별

### 시간 복잡도

일반적으로 **$O(N)$** 의 시간 복잡도를 가진다. Find 연산 혹은 Union 연산에서 하나라도 최적화를 적용하였을 경우 **$O(log n)$** 정도이다.