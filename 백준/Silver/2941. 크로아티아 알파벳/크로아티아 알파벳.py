# 2941 크로아티아 알파벳

word = input()
alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alpha:
    word = word.replace(i, "*")

print(len(word))