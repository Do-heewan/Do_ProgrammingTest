num, max_num = map(int, input().split())
card = list(map(int, input().split()))
l = len(card)

sum_list = []
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            sum = card[i] + card[j] + card[k]
            if (sum <= max_num):
                sum_list.append(sum)

print(max(sum_list))