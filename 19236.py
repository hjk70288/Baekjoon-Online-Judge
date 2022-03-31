# 청소년 상어
import sys
from copy import deepcopy

# 데이터 입력
matrix = [[] for _ in range(4)] # 상어 ['S', 방향], 빈공간 ['E', 'E'], 물고기 [번호, 방향]
inputData = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(4)]
for i in range(4):
  for j in range(4):
    matrix[i].append([inputData[i][j * 2], inputData[i][j * 2 + 1] - 1])

# 상 부터 반시계 방향으로 45도 회전
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 해방 번호 물고기의 위치를 찾음
def findFishPoint(fish, fishNumber):
  for i in range(4):
    for j in range(4):
      if fish[i][j][0] == fishNumber:
        return (i, j, fish[i][j][1])
  return 'False'

# 물고기를 이동시킴
def moveFish(arr):
  # 1번 물고기부터 16번 물고기까지 차례대로 옮김
  for i in range(1, 17):
    fishPoint = findFishPoint(arr, i)

    # 해당 번호의 물고기가 상어에게 먹힌 경우
    if fishPoint == 'False':
      continue
    # 물고기가 아직 먹히지 않은 경우
    else:
      fishX, fishY, direction = fishPoint[0], fishPoint[1], fishPoint[2]

      for _ in range(8):
        nextX, nextY = fishX + dx[direction], fishY + dy[direction]

        if nextX >= 0 and nextX < 4 and nextY >= 0 and nextY < 4: # 공간의 경계를 넘지 않고
          if arr[nextX][nextY][0] != 'S': # 상어가 없다면
            # 둘의 위치를 바꿈
            arr[fishX][fishY][1] = direction
            tempNextValue = arr[nextX][nextY]
            arr[nextX][nextY] = arr[fishX][fishY]
            arr[fishX][fishY] = tempNextValue
            break
        direction += 1 if direction < 7 else -7
  return arr

# 상어를 이동시켜 물고기 먹기
def eatFish(arr, sharkX, sharkY, sumEatFish):
  global maxEatFish
  fish = deepcopy(arr)

  # 물고기 먹기
  sumEatFish += fish[sharkX][sharkY][0]
  direction = fish[sharkX][sharkY][1]
  fish[sharkX][sharkY] = ['S', direction]

  # 물고기 이동
  moveFish(fish)

  # 상어가 이동할 수 있는 위치 후보를 구함
  movablePoint = [] # 상어가 이동할 수 있는 위치 후보
  nextX, nextY = sharkX, sharkY 
  for _ in range(3):
    nextX, nextY = nextX + dx[direction], nextY + dy[direction]
    if nextX >= 0 and nextX < 4 and nextY >= 0 and nextY < 4: # 공간의 경계를 넘지 않고
      if fish[nextX][nextY][0] != 'E': # 빈 공간이 아니라면
        # 이동 가능
        movablePoint.append((nextX, nextY))

  # 이동 가능한 위치가 없다면 재귀 종료
  if len(movablePoint) == 0:
    # 최대값 구하기
    if maxEatFish < sumEatFish:
      maxEatFish = sumEatFish
    return 0

  # 이동 가능한 위치를 모두 탐색해봄
  for point in movablePoint:
    fish[sharkX][sharkY] = ['E', 'E'] # 상어가 있던 위치를 빈공간으로 
    eatFish(fish, point[0], point[1], sumEatFish)

maxEatFish = 0
eatFish(matrix, 0, 0, 0)
print(maxEatFish)