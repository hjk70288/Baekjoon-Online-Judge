# 탈출
import sys 
import copy
from collections import deque

# 데이터 입력
n, m = map(int, sys.stdin.readline().split(' '))
matrix = [list(sys.stdin.readline().strip()) for _ in range(n)] # 물이 퍼지는데 걸리는 시간 정보를 담는 배열
resultMatrix = copy.deepcopy(matrix) # 이동 소요시간 정보를 담는 배열
queue = deque()

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 물이 퍼지는데 소요되는 시간을 계산
def extendWater():
  while(queue):
    visitX, visitY = queue.popleft()

    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]

      if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
        nextObj = matrix[nextX][nextY]
        if nextObj == '.':
          queue.append((nextX, nextY))
          matrix[nextX][nextY] = matrix[visitX][visitY] + 1

# 고슴도치가 이동하는데 걸리는 시간을 구함
def moveHedgehog(x, y):
  queue = deque()
  queue.append((x, y))
  resultMatrix[x][y] = 0 # 고슴도치의 위치의 값을 0으로 초기 설정

  while(queue):
    visitX, visitY = queue.popleft()
    time = resultMatrix[visitX][visitY]

    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]

      if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
        nextObj = matrix[nextX][nextY]
        # D에 도달한 경우 결과값 리턴
        if nextObj == 'D':
          return time + 1
        # 이동 가능한 영역이며, 물이 퍼지지 않은 경우 고슴도치 이동
        if ((nextObj == '.' and resultMatrix[nextX][nextY] == '.') or
            (nextObj != '.' and nextObj != 'X' and nextObj != 'S' and time + 1 < nextObj and resultMatrix[nextX][nextY] == '.')):
          queue.append((nextX, nextY)) 
          resultMatrix[nextX][nextY] = resultMatrix[visitX][visitY] + 1
  # 고슴도치가 D로 도달할 수 없는 경우 리턴          
  return 'KAKTUS'

# 물의 위치 저장
for i in range(n):
  for j in range(m):
    if matrix[i][j] == '*':
      matrix[i][j] = 0
      queue.append((i, j))

extendWater()

for i in range(n):
  for j in range(m):
    if matrix[i][j] == 'S':
      print(moveHedgehog(i, j))
