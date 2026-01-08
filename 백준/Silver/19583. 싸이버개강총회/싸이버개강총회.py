# 19538 싸이버개강총회

import sys
input = sys.stdin.readline

def timetoint(time):
    return int(time.replace(":", ""))

S, E, Q = input().split()
start = timetoint(S)
end = timetoint(E)
streaming = timetoint(Q)

attend = set()
exit = set()
while True:
    try:
        time, name = input().split()
        time = timetoint(time)

        if time <= start:
            attend.add(name)
        elif end <= time <= streaming:
            exit.add(name)

    except:
        break

print(len(attend.intersection(exit)))