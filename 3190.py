# 뱀
import sys
from collections import deque

# 데이터 입력
N = int(sys.stdin.readline())
apple = [[0 for _ in range(N)] for _ in range(N)]
apple[0][0] = 2 # 뱀이 존재하는 곳은 2

K = int(sys.stdin.readline())
for _ in range(K):
  R, C = map(int, sys.stdin.readline().split(' '))
  apple[R - 1][C - 1] = 1 # 사과가 존재하는 곳은 1

L = int(sys.stdin.readline())
turnInfo = []
for _ in range(L):
  X, C = sys.stdin.readline().strip().split(' ')
  turnInfo.append((int(X), C))

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 방향 전환
def turnLeft(direction):
  if direction == 0:
    return 3
  elif direction ==1:
    return 0
  elif direction ==2:
    return 1
  elif direction ==3:
    return 2
# 오른쪽으로 방향 전환
def turnRight(direction):
  if direction == 0:
    return 1
  elif direction ==1:
    return 2
  elif direction ==2:
    return 3
  elif direction ==3:
    return 0

direction = 1 # 뱀이 이동하는 방향 (초기값은 오른쪽)
time = 0 # 게임 진행 시간
x, y = 0, 0 # 뱀의 초기 위치
snake = deque() # 뱀(꼬리 + 몸통)이 존재하는 위치 정보
snake.append((x, y))

# 게임 진행
while True:
  nextX, nextY = x  + dx[direction], y + dy[direction]

  if nextX >= 0 and nextX < N and nextY >=0 and nextY < N and apple[nextX][nextY] != 2:
    # 다음 칸이 사과가 아닌 경우
    if apple[nextX][nextY] != 1:
      tailX, tailY = snake.popleft() # 뱀의 꼬리 위치 반환
      apple[tailX][tailY] = 0 # 뱀의 꼬리 위치를 0으로 변경

   # 뱀을 다음 칸으로 이동   
    apple[nextX][nextY] = 2
    snake.append((nextX, nextY))
    x, y = nextX, nextY
    time += 1

    # 방향 전환을 해야하는 경우
    if len(turnInfo) > 0 and turnInfo[0][0] == time:
      # 왼쪽으로 방향 전환
      if turnInfo[0][1] == 'L':
        direction = turnLeft(direction)
      # 오른쪽으로 방향 전환
      else:
        direction = turnRight(direction)
      turnInfo.pop(0)
  else:
    print(time + 1)
    break