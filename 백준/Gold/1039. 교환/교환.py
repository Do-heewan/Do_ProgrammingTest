# 1039 교환

from collections import deque

def bfs(n: int, k: int) -> int:
    visited = set()
    visited.add((n, 0)) # 초기 값과 0번 변경

    Q = deque()
    Q.append([n, 0])

    ans = 0
    while Q:
        curr, cnt = Q.popleft()

        if cnt == k:
            ans = max(ans, curr)
            continue

        lst = list(str(curr))

        for i in range(len(lst) - 1):
            for j in range(i+1, len(lst)):
                if i == 0 and lst[j] == "0":
                    continue

                lst[i], lst[j] = lst[j], lst[i]
                change_num = int(''.join(lst))

                if (change_num, cnt+1) not in visited:
                    Q.append([change_num, cnt+1])
                    visited.add((change_num, cnt+1))

                lst[i], lst[j] = lst[j], lst[i]

    return ans if ans else -1

N, K = map(int, input().split())
print(bfs(N, K))