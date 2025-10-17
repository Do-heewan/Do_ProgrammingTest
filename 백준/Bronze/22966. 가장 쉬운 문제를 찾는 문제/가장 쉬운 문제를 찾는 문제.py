N = int(input())
lst = []
for _ in range(N):
    lst.append(list(input().split()))

lst.sort(key=lambda x : x[1])
print(lst[0][0])