def solution(routes):
    routes.sort(key=lambda x : x[1])
    
    camera = 1
    check = routes[0][1]
    for start, end in routes:
        if start <= check:
            continue
        
        else:
            check = end
            camera += 1
    
    return camera