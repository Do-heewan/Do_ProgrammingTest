num = int(input())

for i in range(1, num + 1): # i는 1부터 num까지,
    integer = sum(map(int, str(i))) # i의 각 자리수의 합
    num_sum = i + integer # 분해합 = 생성자 + 각 자리수의 합

    if (num == num_sum):    # num_sum과 num이 같을 경우,
        print(i)
        break
    if (i == num):
        print(0)
