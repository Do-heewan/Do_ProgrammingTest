ans = []
for _ in range(5):
    ans.append(int(input()))

ans.sort()

print(int(sum(ans) / len(ans)))
print(ans[2])