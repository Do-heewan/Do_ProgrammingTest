import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    
    if max(N, M) < K*2:
        print("Yuto")
    else:
        if N*M % 2 == 1:
            print("Yuto")
        else:
            print("Platina")