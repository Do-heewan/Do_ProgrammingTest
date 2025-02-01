import sys
input = sys.stdin.readline

H, M = map(int, input().split())

HH = (H - 9) * 60
MM = M

print(HH+MM)