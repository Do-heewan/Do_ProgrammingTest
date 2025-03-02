# 1620 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = {}
for i in range(1, N+1):
    a = input().rstrip()
    # 이름 - 번호 / 번호 - 이름 관계 모두 저장
    pokemon[i] = a
    pokemon[a] = i

for _ in range(M):
    ans = input().rstrip()

    # 입력받은 ans가 정수일 경우
    if (ans.isdigit()):
        print(pokemon[int(ans)])
    # 정수가 아닐 경우 (문자열)
    else:
        print(pokemon[ans])