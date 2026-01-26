# 4635 Speed Limit

while True:
    N = int(input())

    if N == -1:
        break

    mile = 0
    start_time = 0
    for _ in range(N):
        speed, time = map(int, input().split())

        mile += speed * (time - start_time)
        start_time = time

    print(mile, "miles")