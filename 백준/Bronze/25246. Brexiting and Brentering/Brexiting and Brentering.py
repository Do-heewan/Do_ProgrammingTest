word = input().strip()
vowels = {'a', 'e', 'i', 'o', 'u'}

last_vowel_idx = -1
for i in range(len(word)):
    if word[i] in vowels:
        last_vowel_idx = i

print(word[:last_vowel_idx + 1] + "ntry")