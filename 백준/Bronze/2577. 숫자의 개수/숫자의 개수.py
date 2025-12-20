num = 1
for _ in range(3):
    num *= int(input())

num_list = [0 for _ in range(10)]
for n in str(num):
    num_list[int(n)] += 1

for ix in num_list:
    print(ix)