# 2309 일곱 난쟁이

height = []
for _ in range(9):
    height.append(int(input()))
height.sort()

total = sum(height)
for i in range(8):
    for j in range(i+1, 9):
        if total - height[i] - height[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else:
                    print(height[k])
                    
            exit()