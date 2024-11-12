hour, minute, second = map(int, input().split())
time = int(input()) # 초 단위 입력

new_second = second + time
new_minute = minute + new_second // 60
new_hour = hour + new_minute // 60

if (new_second > 59):
    new_second = new_second % 60
    if (new_second == 60):
        new_second = 0
if (new_minute > 59):
    new_minute = new_minute % 60
    if (new_minute == 60):
        new_minute = 0
if (new_hour > 23):
    new_hour = new_hour % 24

print(new_hour, new_minute, new_second)