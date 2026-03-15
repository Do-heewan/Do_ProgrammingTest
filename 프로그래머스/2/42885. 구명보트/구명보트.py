def solution(people, limit):
    people.sort()
    
    left = 0
    right = len(people)-1
    
    boat = 0
    while left <= right:
        curr_weight = people[left] + people[right]
        
        if curr_weight > limit:
            boat += 1
            right -= 1
            
        else:
            boat += 1
            left += 1
            right -= 1
            
    return boat
