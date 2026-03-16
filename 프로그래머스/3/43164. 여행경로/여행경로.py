from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
    
    for v in graph.values():
        v.sort()
        
    route = ["ICN"]
    n = len(tickets)
    
    def dfs(curr):
        if len(route) == n + 1:
            return True
        
        for i in range(len(graph[curr])):
            next_ = graph[curr].pop(i)
            route.append(next_)
            
            if dfs(next_):
                return True
            
            route.pop()
            graph[curr].insert(i, next_)
        
        return False
    
    dfs("ICN")
    
    return route