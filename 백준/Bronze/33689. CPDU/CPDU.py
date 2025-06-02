N = int(input())
count = 0

for _ in range(N):
    word = list(input())
    
    if (word[0] == "C"):
        count += 1
        
print(count)