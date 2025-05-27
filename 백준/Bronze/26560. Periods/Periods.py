T = int(input())

for _ in range(T):
    word = input()
    if "." not in word:
        print(word, ".", sep = "")
    else:
        print(word)