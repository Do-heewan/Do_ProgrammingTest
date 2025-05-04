T = int(input())

for _ in range(T):
    word, a, b = input().split()
    word = list(word)
    
    del word[int(a):int(b)]
    
    for ix in word:
        print(ix, end='')
    print()