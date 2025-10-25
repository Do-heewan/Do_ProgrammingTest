# 30805 사전 순 최대 공통 부분 수열

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

res = []
while True:
    sort_n = sorted(n_list, reverse=True)

    maxA = -1
    for ix in sort_n:
        if ix in m_list:
            maxA = ix
            break
    
    # 부분수열이 존재하지 않을 때
    if maxA == -1:
        break
    
    res.append(maxA)

    n_index = n_list.index(maxA)
    m_index = m_list.index(maxA)

    n_list = n_list[n_index+1:]
    m_list = m_list[m_index+1:]

print(len(res))
print(*res) if res else None