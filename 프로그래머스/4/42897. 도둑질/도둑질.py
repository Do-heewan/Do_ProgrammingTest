from itertools import combinations

def solution(money):
    def count(arr):
        l = len(arr)
        if l == 1:
            return arr[0]
        
        dp = [0] * l
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for i in range(2, l):
            dp[i] = max(dp[i-1], dp[i-2]+arr[i])
            
        return max(dp)
    
    case1 = count(money[:-1])
    case2 = count(money[1:])
    
    return max(case1, case2)