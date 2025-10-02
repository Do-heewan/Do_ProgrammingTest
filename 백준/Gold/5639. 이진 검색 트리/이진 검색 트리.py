# 5639 이진 검색 트리

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

def bst(lst):
    if len(lst) == 0:
        return

    tempL, tempR = [], []

    mid = lst[0]

    for i in range(1, len(lst)):
        if lst[i] > mid:
            tempL = lst[1:i]
            tempR = lst[i:]
            break
    else:
        tempL = lst[1:]

    bst(tempL)
    bst(tempR)
    print(mid)

tree = []
while True:
    try:
        node = int(input())
        tree.append(node)

    except:
        break

bst(tree)