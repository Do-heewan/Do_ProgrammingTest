# 1990 소수인 팰린드롬

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())

# isPalindrome = []
# for i in range(a, b+1):
#     if str(i) == str(i)[::-1]:
#         isPalindrome.append(i)
if b>10000000 :b=10000000
isPalindrome = [n for n in range(a,b+1)if str(n)==str(n)[::-1]]   

for p in isPalindrome:
    if isPrime(p):
        print(p)
print(-1)