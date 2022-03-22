# 드래곤 커브
import sys

# 데이터 입력
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)] # 그릴 커브의 정보
matrix = [[False for _ in range(101)] for _ in range(101)] # True: 커브가 그려진 곳

# 우, 상, 좌, 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 다음 방향(그릴 방향)을 구함
def calcNextDirection(direction):
  if direction == 3:
    direction = 0
  else:
    direction += 1
  return direction

# 드래곤 커브 그리기
def paintDragonCurve():
  for curveData in data:
    y, x, d, g = curveData[0], curveData[1], curveData[2], curveData[3]

    # 0세대 그리기
    matrix[x][y] = True
    x, y = x + dx[d], y + dy[d]
    matrix[x][y] = True
    directionHistory = [d] # 커브가 그려졌던 방향 기록
    
    # 세대만큼 반복
    for _ in range(g):
      paintedHistory = [] # 현 세대를 그릴 때 방향 기록
      # 현 세대를 그리려면 전 세대가 그려진 방향의 반대부터 참조해야함
      for direction in directionHistory[::-1]:
        nextDirection = calcNextDirection(direction) # 다음 방향(그릴 방향) 구하기
        # 현 세대 그리기
        x, y = x + dx[nextDirection], y + dy[nextDirection]
        matrix[x][y] = True
        paintedHistory.append(nextDirection)
      # 현 세대가 그려졌던 방향을 추가함
      directionHistory += paintedHistory

# 드래곤 커브 내의 정사각형 개수 구하기
def countSquare():
  squareCount = 0
  for i in range(101):
    for j in range(101):
      if matrix[i][j] == True:
        if i + 1 < 101 and j + 1 < 101:
          if matrix[i][j + 1] == True and matrix[i + 1][j] == True and matrix[i + 1][j + 1] == True:
            squareCount += 1
  print(squareCount)

paintDragonCurve()
countSquare()