# 1541 잃어버린 괄호

seq = input().split("-") # -를 기준으로 split

num = []

for ix in seq:
    sum = 0
    tmp = ix.split("+") # -로 나눈 애들 중, +로 다시 나눔

    for i in tmp: # 나눠진 애들은 모두 숫자
        sum += int(i) # 합해준다.
    
    num.append(sum) # 더한 값을 리스트에 저장

n = num[0] # num 리스트에는 모두 정수. 따라서 첫 번째 값에서 다른 값들을 빼준다.

for i in range(1, len(num)):
    n -= num[i]

print(n)