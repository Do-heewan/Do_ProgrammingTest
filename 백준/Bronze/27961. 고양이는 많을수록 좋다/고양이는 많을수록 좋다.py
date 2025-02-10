# 27961 고양이는 많을수록 좋다

N = int(input())

def cat(N):
    magic_count = 0
    cat_num = 1
    
    while (N > cat_num):
        cat_num *= 2
        magic_count += 1

    if (N <= cat_num):
        return magic_count + 1

print(cat(N) if N != 0 else 0)