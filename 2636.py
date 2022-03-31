# 치즈
import sys
from collections import deque

# 데이터 입력
n, m = map(int, sys.stdin.readline().split(' '))
cheese = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
queue = deque()

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 치즈 녹이기
def meltCheese():
  global prevMeltCount # 이전에 녹은 치즈의 면적
  queue.append((0, 0))
  visited = [[False for _ in range(m)] for _ in range(n)]
  meltPoint = [] # 녹을 치즈의 좌표

  while queue:
    visitX, visitY = queue.popleft()

    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]

      if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
        if visited[nextX][nextY] == False:
          if cheese[nextX][nextY] == 0:
            queue.append((nextX, nextY))
          else:
            meltPoint.append((nextX, nextY))
          visited[nextX][nextY] = True

  # 녹을 치즈가 있다면
  if len(meltPoint) != 0:
    # 치즈 녹이기
    for point in meltPoint:
      cheese[point[0]][point[1]] = 0
    prevMeltCount = len(meltPoint) # 녹인 치즈의 면적
  return len(meltPoint)

time = 0 # 시간
prevMeltCount = 0 # 이전에 녹은 치즈의 면적
while True:
  curMeltCount = meltCheese() # 이번에 녹은 치즈의 면적
  if curMeltCount == 0:
    print(time, prevMeltCount)
    break
  time += 1
    