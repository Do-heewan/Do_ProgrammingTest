import heapq
import sys
input = sys.stdin.readline

N = int(input())
time_list = [tuple(map(int, input().split())) for _ in range(N)]

# 시작 시간을 기준으로 정렬
time_list.sort()

heap = []  # 종료 시간을 저장할 최소 힙
heapq.heappush(heap, time_list[0][1])  # 첫 번째 강의의 종료 시간을 삽입

for i in range(1, N):
    start, end = time_list[i]

    # 현재 가장 빨리 끝나는 회의의 종료 시간이 다음 회의의 시작 시간보다 작거나 같으면 회의실 재사용 가능
    if heap[0] <= start:
        heapq.heappop(heap)  # 사용한 회의실 제거

    heapq.heappush(heap, end)  # 새로운 회의의 종료 시간 추가

# 최소 필요 회의실 개수는 heap에 남아 있는 종료 시간 개수
print(len(heap))
