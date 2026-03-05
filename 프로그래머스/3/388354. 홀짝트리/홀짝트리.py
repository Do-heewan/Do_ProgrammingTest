# from collections import defaultdict
# import sys
# sys.setrecursionlimit(10 ** 6)

# def solution(nodes, edges):
#     def dfs(node, table, state, visited):
#         visited.add(node)
        
#         # 둘 다 홀수
#         if node % 2 == 1 and len(table[node]) % 2 == 1:
#             # 홀노드 수 증가
#             state[0] += 1
#         # 둘 다 짝수
#         if node % 2 == 0 and len(table[node]) % 2 == 0:
#             # 짝노드 수 증가
#             state[1] += 1
#         # 노드번호 홀수, 자식노드 개수 짝수
#         if node % 2 == 1 and len(table[node]) % 2 == 0:
#             # 역홀노드 수 증가
#             state[2] += 1
#         # 노드번호 짝수, 자식노드 개수 홀수
#         if node % 2 == 0 and len(table[node]) % 2 == 1:
#             # 역짝노드 수 증가
#             state[3] += 1

#         for ix in table[node]:
#             if ix in visited:
#                 continue
#             dfs(ix, table, state, visited)
                
#         return
    
#     tables = defaultdict(set)
#     for edge in edges:
#         tables[edge[0]].add(edge[1])
#         tables[edge[1]].add(edge[0])
    
#     visited = set()
#     answer = [0, 0]
#     for node in nodes:
#         if node not in visited:
#             visited.add(node)
#             state = [0, 0, 0, 0] # 홀노드, 짝노드, 역홀노드, 역짝노드
#             dfs(node, tables, state, visited)
            
#             if state[0] + state[1] == 1:
#                 answer[0] += 1
#             elif state[2] + state[3] == 1:
#                 answer[1] += 1
    
#     return answer

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
def solution(nodes, edges):
    # root가 짝수 = root가 아니면 역짝수
    # root가 홀수 = root가 아니면 역홀수
    # root가 역짝수 = root가 아니면 짝수
    # root가 역홀수 = root가 아니면 홀수
    # 홀짝 트리 => root만 홀짝이고, 나머지는 전부 역홀짝이어야 한다.
      # root가 결정되면, 나머지 노드는 전부 leaf가 하나씩 빠지기 때문.
    # 역홀짝 트리 => root만 역홀짝이고, 나머지는 전부 홀짝트리.
    
    def check_node(table, node, visited, stats):
        # stats = [0, 0, 0, 0]. odd노드 개수, even노드 개수, 역홀수노드 개수, 역짝수노드 개수.
        visited.add(node)
        
        # 홀수 노드
        if node % 2 == 1 and len(table[node]) % 2 == 1:
            stats[0] += 1
        # 짝수 노드
        if node % 2 == 0 and len(table[node]) % 2 == 0:
            stats[1] += 1
        # 역홀수 노드
        if node % 2 == 1 and len(table[node]) % 2 == 0:
            stats[2] += 1
        # 역짝수 노드
        if node % 2 == 0 and len(table[node]) % 2 == 1:
            stats[3] += 1
        
        for n in table[node]:
            if n in visited:
                continue
            check_node(table, n, visited, stats)
        return
    
    tables = defaultdict(set)
    for edge in edges:
        node1, node2 = edge[0], edge[1]
        tables[node1].add(node2)
        tables[node2].add(node1)
    
    visited = set()
    answer = [0, 0]
    for node in nodes:
        if node not in visited:
            visited.add(node)
            stats = [0, 0, 0, 0]
            check_node(tables, node, visited, stats)
            # 홀수노드 1, 짝수노드 0일 경우 or 홀수노드 0, 짝수노드 1일 경우 -> 홀짝 트리 가능. 
            #  (홀짝노드를 루트로 선택하면, 나머지 역홀짝노드의 leaf가 1 줄어들면서 전부 홀짝노드가 된다)
            if (stats[0] + stats[1]) == 1:
                answer[0] += 1
            # 역홀수노드 1, 역짝수노드 0일 경우 or 역홀수노드 0, 역짝수노드 1일 경우 -> 역홀짝 트리 가능
            #  역홀짝노드를 root로 선택하면, 나머지 홀짝노드가 전부 역홀짝노드로 변경되기 때문
            if (stats[2] + stats[3]) == 1:
                answer[1] += 1
    return answer