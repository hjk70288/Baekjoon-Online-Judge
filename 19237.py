# 어른 상어
import sys

# 데이터 입력
n, m, k = map(int, sys.stdin.readline().split(' '))
shark = [[] for _ in range(m)]
smell = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
initDirection = list(map(int, sys.stdin.readline().split(' ')))
directionPriority = [[list(map(int, sys.stdin.readline().split(' '))) for _ in range(4)] for _ in range(m)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어 초기 정보 세팅
for i in range(n):
  for j in range(n):
    if smell[i][j] != 0:
      sharkNumber = smell[i][j]
      shark[sharkNumber - 1] = [i, j, initDirection[sharkNumber - 1] - 1]
      smell[i][j] = [sharkNumber - 1, k]

time = 0 # 진행 시간
dieCount = 0 # 죽은 상어의 수
while True:
  # 1000을 넘기면 종료
  if time > 1000:
    print(-1)
    break

  # 상어가 한마리 남은 경우 종료
  if dieCount + 1 == m:
    print(time)
    break

  # 상어 이동시키기
  for sharkIndex in range(m):
    sharkInfo = shark[sharkIndex]
    if sharkInfo == 0:
      continue
    sharkX, sharkY, direction = sharkInfo[0], sharkInfo[1], sharkInfo[2]

    existEmpty = False
    # 빈 공간으로 이동하는 경우
    for d in directionPriority[sharkIndex][direction]:
      nextX, nextY = sharkX + dx[d - 1], sharkY + dy[d - 1]

      if nextX >= 0 and nextX < n and nextY >= 0 and nextY < n:
        if smell[nextX][nextY] == 0:
          shark[sharkIndex] = [nextX, nextY, d - 1]
          existEmpty = True
          break
    # 주변에 빈 공간이 없어 냄새가 있는 곳으로 이동하는 경우
    if existEmpty == False:
      for d in directionPriority[sharkIndex][direction]:
        nextX, nextY = sharkX + dx[d - 1], sharkY + dy[d - 1]

        if nextX >= 0 and nextX < n and nextY >= 0 and nextY < n:
          if smell[nextX][nextY][0] == sharkIndex:
            shark[sharkIndex] = [nextX, nextY, d - 1]
            break
    
  # 냄새 줄이기
  for i in range(n):
    for j in range(n):
      # 냄새가 있는 공간인 경우
      if smell[i][j] != 0:
        # 냄새가 없어지는 경우
        if smell[i][j][1] - 1 == 0:
          # 냄새 없앰
          smell[i][j] = 0
        # 냄새가 그대로인 경우
        else:
          # 냄새 줄임
          smell[i][j] = [smell[i][j][0], smell[i][j][1] - 1]

  # 상어 냄새 갱신 및 상어 죽이기
  for sharkIndex in range(m):
    sharkInfo = shark[sharkIndex]
    if sharkInfo == 0:
      continue
    sharkX, sharkY = sharkInfo[0], sharkInfo[1]

    # 빈 공간으로 상어가 이동한 경우
    if smell[sharkX][sharkY] == 0:
      smell[sharkX][sharkY] = [sharkIndex, k]
    else:
      # 서로 다른 상어가 같은 공간에 있는 경우
      if smell[sharkX][sharkY][0] != sharkIndex:
        # 상어를 죽임 (1번 상어부터 이동하므로 나중에 이 조건문에 걸린 상어가 죽음)
        shark[sharkIndex] = 0
        dieCount += 1
      # 자신의 냄새가 있는 곳으로 이동한 경우
      elif smell[sharkX][sharkY][0] == sharkIndex:
        smell[sharkX][sharkY] = [sharkIndex, k]
  # 시간 더하기
  time += 1