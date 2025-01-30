# 1874 스택 수열

import sys

input = sys.stdin.readline
N = int(input())

stack = [] # 스택
operate = [] # push(+), pop(-) 여부 저장
count = 1 # 1 ~ N까지 수열 저장
boolean = True # 수열 출력 가능 여부 판단

for _ in range(N):
    num = int(input())

    while (count <= num): # 1부터 num까지 스택에 push
        stack.append(count)
        operate.append("+")

        count += 1

    if (stack[-1] == num): # 스택의 top이 num과 같다면 pop
        stack.pop()
        operate.append("-")

    else: # 같지 않다면 이 수열은 만들 수 없음
        boolean = False

if (boolean):
    for ix in operate:
        print(ix)
else:
    print("NO")