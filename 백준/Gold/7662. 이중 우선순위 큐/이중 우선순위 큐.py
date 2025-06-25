# 7662 이중 우선순위 큐

import heapq

# 삭제할 데이터가 있는지 체크하는 함수
def isEmpty(nums):
	# nums에 1인 데이터가 하나라도 있으면 비어있지 않은 것
    for item in nums:
        if item[1] > 0:
            return False
    return True

T = int(input())

for _ in range(T):
    max_heap = [] # 최대 힙
    min_heap = [] # 최소 힙
    nums = {} # 힙의 값이 삭제될 때, 정보를 공유
    
    k = int(input())
    for _ in range(k):
        cmd, cmd2 = input().split()
        num = int(cmd2)

        # Insert
        if (cmd == "I"):
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
                heapq.heappush(min_heap, num) # 최소 힙에는 숫자 그대로
                heapq.heappush(max_heap, -num) # 최대 힙에는 숫자에 -를 붙혀서

        # Delete
        elif (cmd == "D"):
            if not isEmpty(nums.items()):
                if (num == 1):
                    while (-max_heap[0] not in nums) or (nums[-max_heap[0]] < 1):
                        temp = -heapq.heappop(max_heap)
                        
                        if (temp in nums):
                            del(nums[temp])
                    nums[-max_heap[0]] -= 1
                
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[min_heap[0]] -= 1

    # 결과 출력           
    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])