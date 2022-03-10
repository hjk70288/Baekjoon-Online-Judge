# 벽 부수고 이동하기 4
import copy
import sys
from collections import deque

# 데이터 입력
n, m  = map(int, sys.stdin.readline().split(' '))
originMatrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)] # 원본 데이터
zeroAreaMatrix = copy.deepcopy(originMatrix) # 0끼리 인접되어있는 영역을 표시하기 위한 데이터
zeroAreaInfo = {} # 0끼리 인접되어있는 영역 별 크기 정보

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs 탐색으로 0끼리 인접되어있는 영역의 크기를 구함
def calcZeroAreaSize(x, y, areaName):
  areaSize = 1 # 영역 크기
  queue = deque()
  queue.append((x, y))
  zeroAreaMatrix[x][y] = areaName

  while(queue):
    visitX, visitY = queue.popleft()
    
    # 상 우 하 좌 시계방향 이동
    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]

      if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
        if zeroAreaMatrix[nextX][nextY] == 0:
            areaSize += 1
            queue.append((nextX, nextY))
            zeroAreaMatrix[nextX][nextY] = areaName
  zeroAreaInfo[areaName] = areaSize
  
# 이동가능한 칸의 크기 구하기
def calcMoveableCount(x, y):
  count = 1
  checkedArea = []
    
  # 상 우 하 좌 시계방향 이동
  for d in range(4):
    nextX, nextY = x + dx[d], y + dy[d]

    if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
      if originMatrix[nextX][nextY] == 0: # 벽이 아니라면
        areaName = zeroAreaMatrix[nextX][nextY]
        if not areaName in checkedArea: # 해당 0 영역에 처음 접근했다면
          count += zeroAreaInfo[areaName] # 해당 0 영역의 크기를 더함
          checkedArea.append(areaName)
  originMatrix[x][y] = str(count % 10) # 결과 값 세팅
  
areaNumber = 0 # 0 영역의 Index
for i in range(n):
  for j in range(m):
    if zeroAreaMatrix[i][j] == 0:
      calcZeroAreaSize(i, j, 'a' + str(areaNumber))
      areaNumber += 1

for i in range(n):
  for j in range(m):
    if originMatrix[i][j] == 1:
      calcMoveableCount(i, j)

for i in range(n):
  print(''.join(str(_) for _ in originMatrix[i]))