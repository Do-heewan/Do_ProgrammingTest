def hanoi(n, base, target, sub):
    global count
    count += 1

    if (n == 1):
        print(base, "->",target)
        return 
    
    hanoi(n-1, base, sub, target)
    print(base, "->", target)
    hanoi(n-1, sub, target, base)

N = int(input())
count = 0
hanoi(N, 1, 3, 2)
print(count)