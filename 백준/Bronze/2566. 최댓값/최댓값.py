# 2566 최댓값

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

max_val = 0
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_val:
            max_val = arr[i][j]
            x = i+1
            y = j+1

print(max_val)
print(x, y)