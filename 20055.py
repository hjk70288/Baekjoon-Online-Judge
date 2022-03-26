# 컨베이어 벨트 위의 로봇
import sys
from collections import deque

# 데이터 입력
n, k = map(int, sys.stdin.readline().split(' '))
belt = deque(map(int, sys.stdin.readline().split(' '))) # 컨베이어 벨트 내구도
robots = deque(False for _ in range(2 * n)) # 로봇이 존재하는 위치: True
global zeroBelt # 내구도가 0인 벨트의 개수
zeroBelt = 0

# 벨트 회전시키기
def rotationBelt():
  # 벨트를 회전시킴
  lastBelt = belt.pop()
  belt.appendleft(lastBelt)

  # 로봇의 위치도 같이 옮겨줌
  lastRobot = robots.pop()
  robots.appendleft(lastRobot)

  # 로봇이 내리는 위치에 도달한 경우 로봇 내리기
  if robots[n - 1] ==  True:
    robots[n - 1] = False

# 로봇 이동시키기
def moveRobot():
  global zeroBelt
  for i in range(n - 1, -1, -1):
    # 해당 위치에 로봇이 존재하는 경우
    if robots[i] == True:
      nextBeltIndex = i + 1
      # 다음 위치에 로봇이 존재하지 않고 내구도가 0 이상이면
      if robots[nextBeltIndex] == 0 and belt[nextBeltIndex] != 0:
        # 로봇의 위치를 옮기고 내구도 감소시키기
        robots[i] = False
        robots[nextBeltIndex] = True
        belt[nextBeltIndex] -= 1
        if belt[nextBeltIndex] == 0:
          zeroBelt += 1
      # 로봇이 내리는 위치에 도달한 경우 로봇 내리기
      if nextBeltIndex == n - 1:
        robots[nextBeltIndex] = False

# 올리는 위치에 로봇 올리기
def setRobot():
  global zeroBelt
  if belt[0] != 0:
    robots[0] = True
    belt[0] -= 1
    if belt[0] == 0:
      zeroBelt += 1

count = 0 # 단계
while True:
  count += 1
  rotationBelt()
  moveRobot()
  setRobot()
  if zeroBelt >= k:
    break
print(count)