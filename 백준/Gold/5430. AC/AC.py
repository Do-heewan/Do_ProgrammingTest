# 5430 AC

import sys
from collections import deque
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func = input().rstrip()
    num = int(input())
    arr = input().rstrip()
    
    Q = deque(arr[1:-1].split(","))

    if (num == 0):
        Q = deque()

    is_Null = False
    rev = 0

    for cmd in func:
        if (cmd == "R"):
            rev += 1
        elif (cmd == "D"):
            if Q:
                if (rev % 2 != 0):
                    Q.pop()
                else:
                    Q.popleft()
            else:
                print("error")
                is_Null = True
                break

    if not is_Null:
        if (rev % 2 != 0):
            Q.reverse()
            print("[" + ",".join(Q) + "]")
        else:
            print("[" + ",".join(Q) + "]")