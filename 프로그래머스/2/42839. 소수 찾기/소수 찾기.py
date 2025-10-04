from itertools import permutations

def is_prime(x):
    if(x <= 1):
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False    
    return True

def solution(numbers):
    answer = 0
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers)+1):
        per += (list(permutations(nums, i)))
    new_nums = [int(("").join(p)) for p in per]
    
    new_nums = list(set(new_nums))
    
    cnt = 0
    for ix in new_nums:
        if is_prime(ix):
            cnt += 1 
        
    return cnt

