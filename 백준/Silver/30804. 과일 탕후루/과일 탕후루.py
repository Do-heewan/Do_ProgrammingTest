# 30804 과일 탕후루

N = int(input())
fruit = list(map(int, input().split()))

start = 0 # 시작 점
fruit_count = {} # 과일 종류 담는 딕셔너리
max_len = 0 # 최대 길이

for end in range(N):
    curr_fruit = fruit[end] # 현재 과일

    # 현재 과일이 딕셔너리에 존재 하는지
    if curr_fruit in fruit_count:
        fruit_count[curr_fruit] += 1
    else:
        fruit_count[curr_fruit] = 1
    
    # 과일 종류가 2개 이상일 경우
    while (len(fruit_count) > 2):
        del_fruit = fruit[start] # 제거할 과일

        fruit_count[del_fruit] -= 1 # 과일 하나 제거

        if (fruit_count[del_fruit] == 0): # 만약 과일 개수가 0개가 되면
            del fruit_count[del_fruit] # 목록에서 제거

        start +=1 # 시작 점 증가
    
    max_len = max(max_len, end - start + 1) # 탕후루 길이

print(max_len)