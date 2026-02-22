# 1021 회전하는 큐

from collections import deque

def left_move(queue):
  element = queue.popleft()
  queue.append(element)
  return queue

def right_move(queue):
  element = queue.pop()
  queue = [element] + list(queue)
  return deque(queue)

N, M = map(int, input().split())
targets = deque(map(int, input().split()))

queue = deque(range(1, N+1))
total_moves = 0

for target in targets:
  while True:
    if queue[0] == target:
      queue.popleft()
      break

    else:
      idx = queue.index(target)

      if idx <= len(queue) // 2:
        queue = left_move(queue)
        total_moves += 1

      else:
        queue = right_move(queue)
        total_moves += 1

print(total_moves)