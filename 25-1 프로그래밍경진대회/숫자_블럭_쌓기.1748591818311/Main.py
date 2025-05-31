N = int(input())

stack = []
pre_stack = []
count = 0

for _ in range(2*N):
	cmd = input()

	if (cmd[:3] == "add"):
		cmd, num = cmd.split()

	if (cmd == "add"):
		pre_stack.append(int(num))

	elif (cmd == "remove"):
		# pre_stack에서 pop될 수가 가장 작은 수인지 판별
		if not (pre_stack[-1] == min(pre_stack)):
			pre_stack.sort(reverse = True)
			count += 1
		
		a = pre_stack.pop()
		stack.append(a)

print(count)