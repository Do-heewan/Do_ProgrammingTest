def solution(n, w, num):
    height = n // w if n % w == 0 else n // w + 1
    boxes = []
    for i in range(height):
        temp = []
        for j in range(1, w+1):
            temp.append(j + i*w if j + i*w <= n else 0)
        boxes.append(temp)
    
    for i in range(height):
        if i % 2 == 1:
            boxes[i].reverse()
    
    
    target_x, target_y = 0, 0
    for y in range(height):
        for x in range(w):
            if boxes[y][x] == num:
                target_y = y; target_x = x
    
    ans = 0
    for h in range(target_y, height):
        if boxes[h][target_x]:
            ans += 1
            
    return ans