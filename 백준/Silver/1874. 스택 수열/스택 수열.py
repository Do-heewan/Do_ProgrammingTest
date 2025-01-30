# 1874 스택 수열

N = int(input())

stack = []
operate = []
count = 1
boolean = True

for _ in range(N):
    num = int(input())

    while (count <= num):
        stack.append(count)
        operate.append("+")

        count += 1

    if (stack[-1] == num):
        stack.pop()
        operate.append("-")

    else:
        boolean = False

if (boolean):
    for ix in operate:
        print(ix)
else:
    print("NO")