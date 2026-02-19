# 1036 36진수

def convertToInt(word):
    if '0' <= word <= '9':
        return ord(word) - ord('0')
    return ord(word) - ord('A') + 10

def convertToStr(num):
    if num < 10:
        return chr(num+ord('0'))
    return chr(num-10+ord('A'))

def baseTo36(num):
    if num == 0:
        return 0

    res = ''
    while num != 0:
        res += convertToStr(num % 36)
        num //= 36

    return res[::-1]

N = int(input())
words = list(input() for _ in range(N))
K = int(input())

gain = [0] * 36
total = 0

for word in words:
    num = 0
    L = len(word)

    for i in range(L):
        curr = convertToInt(word[i])
        idx = L-(i+1)

        gain[curr] += (35-curr) * 36 ** idx
        num = num * 36 + curr
    total += num

gain = sorted(gain, reverse=True)
total += sum(gain[:K])

print(baseTo36(total))