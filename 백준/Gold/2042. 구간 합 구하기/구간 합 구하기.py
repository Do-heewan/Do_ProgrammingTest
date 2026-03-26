# 2042 구간 합 구하기

import sys
input = sys.stdin.readline

import math

def segment(left, right, idx=1):
    if left == right:
        segment_tree[idx] = nums[left]
        return segment_tree[idx]
    mid = (left+right) // 2
    segment_tree[idx] = segment(left, mid, idx*2) + segment(mid+1, right, idx*2+1)
    return segment_tree[idx]

def query_sum(start, end, left, right, idx=1):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[idx]
    
    mid = (start+end) // 2
    return query_sum(start, mid, left, right, idx*2) + query_sum(mid+1, end, left, right, idx*2+1)

def update(start, end, idx, diff, i=1):
    if idx < start or idx > end:
        return
    segment_tree[i] += diff
    
    if start != end:
        mid = (start+end) // 2
        update(start, mid, idx, diff, i*2)
        update(mid+1, end, idx, diff, i*2+1)

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

n = len(nums)
H = math.ceil(math.log(n, 2))
tree_size = pow(2, H+1)-1
segment_tree = [0] + [0] * tree_size

segment(0, n-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    # b -> c로 변경
    if a == 1:
        diff = c - nums[b-1]
        nums[b-1] = c
        update(0, n-1, b-1, diff, 1)
    
    # b~c까지의 합 출력
    elif a == 2:
        print(query_sum(0, n-1, b-1, c-1, 1))
