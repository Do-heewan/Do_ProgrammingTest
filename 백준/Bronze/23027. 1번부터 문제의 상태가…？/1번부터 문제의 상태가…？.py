word = list(input())

if "A" in word:
    for i in range(len(word)):
        if (word[i] == "B") or (word[i] == "C") or (word[i] == "D") or (word[i] == "F"):
            word[i] = "A"
elif "B" in word:
    for i in range(len(word)):
        if (word[i] == "C") or (word[i] == "D") or (word[i] == "F"):
            word[i] = "B"
elif "C" in word:
    for i in range(len(word)):
        if (word[i] == "D") or (word[i] == "F"):
            word[i] = "C"
else:
    for i in range(len(word)):
        word[i] = "A"
        
for ix in word:
    print(ix, end='')