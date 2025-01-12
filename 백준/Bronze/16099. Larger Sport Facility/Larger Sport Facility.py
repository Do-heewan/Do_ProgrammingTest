# 16099 Larger Sport Facility

T = int(input())

for _ in range(T):
    t_w, t_h, e_w, e_h = map(int, input().split())

    if (t_w * t_h < e_w * e_h):
        print("Eurecom")
    elif (t_w * t_h > e_w * e_h):
        print("TelecomParisTech")
    else:
        print("Tie")