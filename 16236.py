# 아기 상어
import sys
from collections import deque

# 데이터 입력
n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 상, 좌, 하, 우 (반시계방향)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 먹을 수 있는 물고기를 찾음
def findEatAbleFish(x, y):
  visited = [[-1 for _ in range(n)] for _ in range(n)]
  visited[x][y] = 0
  queue = deque()
  queue.append((x, y))
  eatAbleFish = [] # 먹을 수 있는 물고기들의 정보 (거리, 좌표)

  # BFS 탐색
  while queue:
    visitX, visitY = queue.popleft()

    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]

      if nextX >= 0 and nextX < n and nextY >=0 and nextY < n:
        # 방문하지 않았고, 빈칸이거나 이동할 수 있는 경우
        if visited[nextX][nextY] == -1 and (matrix[nextX][nextY] == 0 or sharkSize >= matrix[nextX][nextY]):
          visited[nextX][nextY] = visited[visitX][visitY] + 1
          queue.append((nextX, nextY))

          # 먹을 수 있는 물고기에 도달한 경우
          if matrix[nextX][nextY] != 0 and sharkSize > matrix[nextX][nextY]:
            # 먹을 수 있는 물고기 정보 갱신
            eatAbleFish.append((visited[nextX][nextY], nextX, nextY))
  # 먹을 수 있는 물고기가 있는 경우 거리, x 좌표, y 좌표에 대해 오름차순으로 정렬 후 첫번 째 요소 반환
  return False if len(eatAbleFish) == 0 else sorted(eatAbleFish)[0]

sharkSize = 2 # 상어의 크기
eatCount = 0 # 상어가 먹은 물고기 수
moveResult = 0 # 이동한 총 거리
sharkX, sharkY = 0, 0 # 상어가 있는 위치
for i in range(n):
  for j in range(n):
    # 아기 상어의 위치 저장
    if matrix[i][j] == 9:
      sharkX, sharkY = i, j

while True:
  matrix[sharkX][sharkY] = 0 # 상어가 있는 곳의 위치를 0으로 초기화
  eatAbleFishInfo = findEatAbleFish(sharkX, sharkY) # 먹을 수 있는 물고기 찾기

  # 먹을 수 있는 물고기가 없는 경우
  if eatAbleFishInfo == False:
    print(moveResult)
    break

  distance, sharkX, sharkY = eatAbleFishInfo # 물고기와의 거리, x 좌표, y 좌표
  moveResult += distance # 결과 값 갱신
  eatCount += 1

  # 상어의 크기만큼 물고기를 먹은 경우
  if sharkSize == eatCount:
    # 먹은 물고기 초기화 및 상어 크기 키우기
    eatCount = 0
    sharkSize += 1
