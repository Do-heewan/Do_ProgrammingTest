# 1764 듣보잡

n, m = map(int, (input().split()))

n_list = set()
m_list = set()

for i in range(n):
    name1 = input()
    n_list.add(name1)
for j in range(m):
    name2 = input()
    m_list.add(name2)

sum_list = n_list & m_list
print(len(sum_list))

sum_list = list(sum_list)
sum_list.sort()
for k in sum_list:
    print(k)