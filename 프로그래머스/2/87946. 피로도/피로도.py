max_count = 0

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    
    
    def dfs(hp, count):
        global max_count
        
        max_count = max(count,max_count)
        for i in range(n):
            now, cost = dungeons[i]
            
            if hp>=now and not visited[i]:
                visited[i] = True
                dfs(hp-cost, count+1)
                visited[i] = False
    dfs(k, 0)
    
    return max_count