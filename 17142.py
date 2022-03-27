# 연구소 3
import sys
from collections import deque
from itertools import combinations

# 데이터 입력
n, m = map(int, sys.stdin.readline().split(' '))
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
virus = [] # 바이러스의 좌표 값
queue = deque()

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0인 곳(바이러스가 퍼지지 않은 영역)의 개수
zeroCount = 0
for i in range(n):
  for j in range(n):
    if matrix[i][j] == 2:
      virus.append((i, j)) # 바이러스 위치 정보 추가
    elif matrix[i][j] == 0:
      zeroCount += 1

# 바이러스 퍼뜨리기
def extendVirus(virusPoint):
  time = 0 # 바이러스가 퍼지는데 소요되는 시간
  extendCount = 0 # 바이러스가 채워진 영역의 개수
  visited = [[-1 for _ in range(n)] for _ in range(n)]

  # 활성화 바이러스 위치 설정
  for point in virusPoint:
    queue.append(point)
    x, y = point[0], point[1]
    visited[x][y] = 0

  while queue:
    visitX, visitY = queue.popleft()

    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]

      if nextX >= 0 and nextX < n and nextY >= 0 and nextY < n:
        if visited[nextX][nextY] == -1 and matrix[nextX][nextY] != 1:
          # 비활성화된 바이러스를 만난 경우
          if visited[nextX][nextY] == -1 and matrix[nextX][nextY] == 2:
            # 바이러스 활성화
            visited[nextX][nextY] = visited[visitX][visitY] + 1
            queue.append((nextX, nextY))
          # 빈 칸을 만난 경우
          else:
            # 바이러스 퍼뜨림, 바이러스 영역 개수 갱신
            visited[nextX][nextY] = visited[visitX][visitY] + 1
            extendCount += 1
            # 바이러스가 퍼지는데 소요되는 시간 갱신
            if time < visited[nextX][nextY]:
              time = visited[nextX][nextY]
            queue.append((nextX, nextY))
  # 바이러스가 모두 퍼졌다면 소요 시간 리턴, 퍼지지 않았다면 불가능 리턴
  return time if zeroCount == extendCount else 'False'
  
result = []
for virusPoint in list(combinations(virus, m)): # 활성화될 바이러스의 조합
  extendResult = extendVirus(virusPoint)
  if extendResult != 'False':
    result.append(extendVirus(virusPoint))
# 결과 출력
if len(result) == 0:
  print(-1)
else:
  print(min(result))
