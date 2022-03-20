# Puyo Puyo
from cgitb import reset
import sys
from collections import deque

# 데이터 입력
matrix = [list(sys.stdin.readline().strip()) for _ in range(12)]
queue = deque()

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 중력을 적용하여 뿌요가 밑으로 내려갈 수 있으면 밑으로 내려가도록 함
def applyGravity():
  # 11번째 줄 부터 1번째 줄 순서로 검사 (맨 밑줄을 제외하고 밑에서부터)
  for i in range(10, -1, -1):
    for j in range(0, 6):
      if matrix[i][j] != '.': # 뿌요인 경우
        puyoColor = matrix[i][j]
        underIndex = i + 1
        underCount = 0
        # .이 아닌 요소를 만날때 까지 검사하여 밑으로 얼마나 내릴 수 있는지 확인
        while True:
          if underIndex < 12 and matrix[underIndex][j] == '.':
            underCount += 1
            underIndex += 1
          else:
            break
        # 밑으로 내릴 수 있는 경우
        if underCount > 0:
          matrix[i][j] = '.' # 원래 있던 뿌요를 .으로 바꾸고
          matrix[underIndex - 1][j] = puyoColor # 뿌요를 밑으로 내림

# 뿌요가 4개 이상 연결되어 있으면 연쇄
def crashPuyo(x, y, color):
  queue.append((x, y))
  visited = [[False for _ in range(6)] for _ in range(12)]
  closePuyo = [(x, y)] # 인접한 뿌요들의 좌표
  visited[x][y] = True
  crash = False # 연쇄 발생 여부
  
  while queue:
    visitX, visitY = queue.popleft()

    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]

      if nextX < 12 and nextX >= 0 and nextY < 6 and nextY >=0:
        if visited[nextX][nextY] == False and matrix[nextX][nextY] == color:
          queue.append((nextX, nextY))
          closePuyo.append((nextX, nextY))
          visited[nextX][nextY] = True
  # 인접한 뿌요의 개수가 4개 이상이라면
  if len(closePuyo) >= 4:
    crash = True # 연쇄 발생
    for i in closePuyo:
      matrix[i[0]][i[1]] = '.'
  return crash

result = 0 # 결과 값 (중력이 적용된 횟수)
while True:
  crashCount = 0 # 한턴에 발생한 연쇄의 횟수
  for i in range(12):
    for j in range(6):
      if matrix[i][j] != '.':
        # 4방향 검사해서 연쇄할 수 있는지 체크 후 연쇄
        if crashPuyo(i, j, matrix[i][j]):
          crashCount += 1

  # 만약 연쇄가 한번도 일어나지 않았다면 종료
  if crashCount == 0:
    break
  # 연쇄가 일어났다면 중력 적용
  else:
    result += 1
    applyGravity()
print(result)