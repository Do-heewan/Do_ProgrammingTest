# 9357 패션왕 신해빈

T = int(input())

for _ in range(T):
    N = int(input())

    wear = {}
    # wear에 키-밸류 형태로 저장
    for _ in range(N):
        clothes, kind = input().split()

        if (kind in wear):
            wear[kind].append(clothes)
            continue

        wear[kind] = [clothes]

    cnt = 1
    
    # 조합식을 세워 계산
    # +1하는 이유는 알몸도 옷이라고 생각해 추가
    for x in wear:
        cnt *= (len(wear[x]) + 1)
	
    # -1하는 이유 모든 종류의 옷을 착용하지 않았을 경우를 제외
    print(cnt-1)