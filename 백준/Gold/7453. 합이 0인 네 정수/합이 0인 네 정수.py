#sol2
import sys;input = sys.stdin.readline
N = int(input())
A = [];B = [];C = [];D = []
for _ in range(N):
    a,b,c,d = map(int,input().split())
    A.append(a);B.append(b);C.append(c);D.append(d)
dic = {}
for a in A:
    for b in B:
        if a+b in dic:dic[a+b]+=1
        else:dic[a+b]=1
ans = 0
for c in C:
    for d in D:
        if -c-d in dic:
            ans+=dic[-c-d]
print(ans)