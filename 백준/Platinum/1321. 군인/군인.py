# 1321 군인

import sys
input = sys.stdin.readline

import math

def segment(left, right, idx):
    if left == right:
        segment_tree[idx] = army[left]
        return segment_tree[idx]
    
    mid = (left+right) // 2
    segment_tree[idx] = segment(left, mid, idx*2) + segment(mid+1, right, idx*2+1)
    return segment_tree[idx]

def query_sum(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[idx]
    
    mid = (start+end) // 2
    return query_sum(start, mid, idx*2, left, right) + query_sum(mid+1, end, idx*2, left, right)

def update(start, end, node, idx, val):
    if start > idx or idx > end:
        return
    segment_tree[node] += val
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node*2, idx, val)
        update(mid+1, end, node * 2 +1, idx, val)

def find_group(start, end, node, number):
    if start == end:
        return start
    
    mid = (start+end) // 2

    if segment_tree[node*2] >= number:
        return find_group(start, mid, node*2, number)
    else:
        return find_group(mid+1, end, node*2+1, number-segment_tree[node*2])


N = int(input())
army = list(map(int, input().split()))
H = math.ceil(math.log(N, 2))
tree_size = pow(2, H+1)-1

segment_tree = [0] + [0] * tree_size
segment(0, N-1, 1)

M = int(input())
for _ in range(M):
    cmd = list(map(int, input().split()))

    # n번 부대 p명 증원,감원
    if cmd[0] == 1:
        n, p = cmd[1], cmd[2]
        update(0, N-1, 1, n-1, p)

    # i번이 어느 부대인지
    elif cmd[0] == 2:
        i = cmd[1]
        print(find_group(0, N-1, 1, i)+1)
