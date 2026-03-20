# 9527 1의 개수 세기

def count_one(n):
    result = 0
    i = 0

    while (1 << i) <= n:
        cycle = 1 << (i+1)

        result += (n+1) // cycle * (1 << i)

        remainder = (n+1) % cycle
        result += max(0, remainder - (1 << i))

        i += 1
    
    return result

A, B = map(int, input().split())
print(count_one(B) - count_one(A-1))