def solution(n, bans):
    alpha = {}
    nums = {}
    for i in range(26):
        alpha[chr(i+ord('a'))] = i+1
        nums[i+1] = chr(i+ord('a'))
        
    num_bans = []
    for b in bans:
        num = 0
        b = b[::-1]
        for i in range(len(b)):
            num += alpha[b[i]] * 26 ** i
        num_bans.append(num)
    
    num_bans.sort()
    for nb in num_bans:
        if nb <= n:
            n += 1
    
    res = ''
    while n != 0:
        n -= 1
        remain = n % 26
        res += nums[remain+1]
        n //= 26
    
    return res[::-1]