N, M = map(int, input().split())
word = input().strip()
A, C, G, T = map(int, input().split())

need = {'A': A, 'C': C, 'G': G, 'T': T}
curr = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# 초기 윈도우 세팅
for i in range(M):
    curr[word[i]] += 1

def check():
    return (curr['A'] >= need['A'] and
            curr['C'] >= need['C'] and
            curr['G'] >= need['G'] and
            curr['T'] >= need['T'])

cnt = 0

if check():
    cnt += 1

# 슬라이딩
for i in range(M, N):
    # 오른쪽 추가
    curr[word[i]] += 1
    # 왼쪽 제거
    curr[word[i - M]] -= 1

    if check():
        cnt += 1

print(cnt)