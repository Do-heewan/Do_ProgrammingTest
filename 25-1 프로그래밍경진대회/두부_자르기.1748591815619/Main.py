# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())

if (N % 2 == 0):
	lst = [x for x in range(N//2, 0, -1)]
else:
	lst = [x for x in range(N//2 + 1, 0, -1)]

result = []
for i in lst:
	set = N
	target = i
	count = 0
	
	while set > target:
		set -= target # N에 target만큼 빼고 횟수를 저장
		count += 1

	result.append([i, count])

print(len(result))