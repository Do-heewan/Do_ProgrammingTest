# 1302 베스트셀러

N = int(input())

books = {}
for _ in range(N):
    name = input()
    books[name] = books.get(name, 0) + 1

maxCount = max(books.values())

ans = []
for k, v in books.items():
    if v == maxCount:
        ans.append(k)

ans.sort()
print(ans[0])