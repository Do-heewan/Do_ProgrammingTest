def solution(N, number):
    dp = [[] for _ in range(9)]
    
    for i in range(1, 9):
        comb_set = set()
        comb_set.add(int(str(N)*i))
        
        for j in range(1, i):
            for comb1 in dp[i-j]:
                for comb2 in dp[j]:
                    plus = comb1 + comb2
                    minus = comb1 - comb2
                    mul = comb1 * comb2
                    
                    comb_set.add(plus)
                    comb_set.add(mul)
                    if minus >= 0:
                        comb_set.add(minus)
                    
                    if comb2 != 0:
                        div = comb1 / comb2
                        if div % 1 == 0:
                            comb_set.add(div)

        if number in comb_set:
            return i

        for c in comb_set:
            dp[i].append(c)

    return -1