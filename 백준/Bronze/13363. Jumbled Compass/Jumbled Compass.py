# 13363

start = int(input())
target = int(input())

# 시계 방향 (오른쪽): target이 start보다 앞에 있으면 360 더하기
right = (target - start) % 360

# 반시계 방향 (왼쪽): 음수로 표현
left = right - 360

# 절댓값이 작은 쪽 선택, 같으면 양수(시계방향) 우선
if abs(left) < abs(right):
    print(left)
else:
    print(right)