import heapq

def solution(n, costs):
    def find_root(x):
        if x == parent[x]: return x
        parent[x] = find_root(parent[x])
        
        return parent[x]
    
    def union(a, b):
        x = find_root(a)
        y = find_root(b)
        
        if x > y:
            parent[x] = y
        else:
            parent[y] = x
            
    def same_root(a, b):
        return find_root(a) == find_root(b)
        
    
    costs.sort(key=lambda x : x[2])
    
    parent = [i for i in range(n)]
    
    res = 0
    for a, b, cost in costs:
        # union-find
        if not same_root(a, b):
            union(a, b)
            res += cost
            
    return res
        
        