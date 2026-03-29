# 6549 히스토그램에서 가장 큰 직사각형

while True:
    lst = list(map(int, input().split()))
    n = len(lst)

    if lst[0] == 0:
        break

    stack = []
    max_square = 0
    for idx, height in enumerate(lst):

        if idx == 0:
            continue
        
        # 더 높은 블럭이 들어오면 넓이 계산
        if stack and stack[-1][1] > height:
            while stack:
                stack_i, stack_height = stack.pop()
                width = 1
                if stack:
                    width = stack[-1][0]+1
                square = (idx - width) * stack_height
                max_square = max(max_square, square)

                if not stack or stack[-1][1] <= height:
                    break

        if not stack or stack[-1][1] <= height:
            stack.append([idx, height])

    while stack:
        stack_i, stack_height = stack.pop()
        width = 1
        if stack:
            width = stack[-1][0]+1
        square = (lst[0]+1 - width) * stack_height
        max_square = max(max_square, square)

    print(max_square)