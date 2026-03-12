import sys
N = int(sys.stdin.readline())
result = []
for i in range(1000): # 1000번의
    result.append(1) # 1
for j in range(1000): # 1000번의
    result.append(1000) # 1000
print(len(result))
print(*result)