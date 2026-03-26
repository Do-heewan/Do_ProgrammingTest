# 1541 잃어버린 괄호

calc = input().split("-")

nums = []
for ix in calc:
    num = 0
    tmp = ix.split("+")

    for t in tmp:
        num += int(t)
    
    nums.append(num)

n = nums[0]

for i in range(1, len(nums)):
    n -= nums[i]

print(n)