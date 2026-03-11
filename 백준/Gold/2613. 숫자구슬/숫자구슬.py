# 2613 숫자구슬

# "각 그룹 합이 mid 이하가 되도록 M개 이하 그룹으로 나눌 수 있는지" 확인
def check(mid):
    count = 1 # 현재 그룹의 갯수
    s = 0 # 현재 그룹의 합

    for num in numbers:
        # 현재 그룹에 num을 더하면 mid값 초과 -> 그룹 수 증가
        if s + num > mid:
            count += 1
            s = num
        # 현재 그룹에 숫자 추가
        else:
            s += num

    # 그룹 갯수가 M개 미만이면 True -> 가능한 조합
    return count <= M

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

left = max(numbers)
right = sum(numbers)

while left <= right:
    mid = (left+right) // 2

    # 현재의 중앙값으로 M개의 그룹을 생성할 수 있다면, 더 작은 값으로도 가능한지 확인
    if check(mid):
        right = mid - 1
    # 아니면 값을 키운다.
    else:
        left = mid + 1

# 이분탐색 종료 후 left의 값 = 최적의 값
answer = left
print(answer)

groups = []

s = 0 # 현재 그룹 합
cnt = 0 # 현재 그룹 구슬 개수

for num in numbers:

    # 현재 그룹에 num을 더했을 때,
    if s + num > answer:
        # answer를 넘는다면 지금까지의 그룹은 확정
        groups.append(cnt)
        # 새로운 그룹 생성
        s = num
        cnt = 1
    
    # answer보다 작다면 현재 그룹에 계속 더해줌
    else:
        s += num
        cnt += 1

# 마지막 그룹 추가
groups.append(cnt)

# 현재 그룹의 개수가 M개 보다 작다면, 구슬이 2개 이상인 그룹에서 분할하여 그룹의 개수를 M개로 맞춰줌
while len(groups) < M:
    for i in range(len(groups)):
        if groups[i] > 1:
            # 그룹을 하나 분리
            groups[i] -= 1

            # 앞에 새로운 그룹 추가
            groups.insert(i, 1)

            break

print(*groups)