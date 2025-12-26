# 4673 셀프 넘버

def make_selfnum(i):
    res = i
    for ix in str(i):
        res += int(ix)

    return res

realNum = set(i for i in range(1, 10001))

selfNum = set()
for i in range(1, 10001):
    selfNum.add(make_selfnum(i))

result = realNum - selfNum
for r in sorted(result):
    print(r)