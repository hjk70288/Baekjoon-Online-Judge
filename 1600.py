# 말이 되고픈 원숭이
import sys
from collections import deque

# 데이터 입력
k = int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().split(' '))
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
queue = deque()

# 위 부터 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
kx = [-2, -1, 1, 2, 2, 1, -1, -2]
ky = [1, 2, 2, 1, -1, -2, -2, -1]

# BFS 탐색을 통한 최단거리 찾아내기
def findShortcut():
  global k
  queue.append((0, 0, k)) # 좌표, 점프 가능 횟수
  # [['점프 0번 가능 시 동작 횟수'] ... ['점프 k-1번 가능 시 동작 횟수'], ['점프 k번 가능 시 동작 횟수']]
  visited = [[['False' for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
  for i in range(k + 1):
    visited[0][0][i] = 0

  ''' 
    점프를 사용하지 않는 경우, 점프를 사용하는 경우 모두를 큐에 넣으면
    점프를 사용하지 않는 좌표 4방향, 점프를 사용한 좌표 4방향 (경계나 벽에 의해 꼭 4방향이 아닐 수도 있음) 이 쌓인다.
     => 모든 좌표에 대해 k ~ 0 번 점프를 사용해서 도달하는데 걸리는 동작 수를 구할 수 있음
  '''
  while queue:
    visitX, visitY, hourse = queue.popleft()

    # 도착 지점에 도달한 경우
    if visitX + 1 == n and visitY + 1 == m:
      print(visited[visitX][visitY][hourse])
      return

    # 점프를 사용하지 않는 경우 (점프를 할 수 있어도 사용하지 않음)
    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]
      if nextX >= 0 and nextX < n and nextY >=0 and nextY < m:
        if visited[nextX][nextY][hourse] == 'False' and matrix[nextX][nextY] != 1:
          queue.append((nextX, nextY, hourse))
          visited[nextX][nextY][hourse] = visited[visitX][visitY][hourse] + 1

    # 점프를 사용할 수 있는 경우
    if hourse > 0:
      for k in range(8):
        nextX, nextY = visitX + kx[k], visitY + ky[k]
        if nextX >= 0 and nextX < n and nextY >=0 and nextY < m:
          if visited[nextX][nextY][hourse - 1] == 'False' and matrix[nextX][nextY] != 1:
            queue.append((nextX, nextY, hourse - 1))
            
            visited[nextX][nextY][hourse - 1] = visited[visitX][visitY][hourse] + 1

  # 도착 지점에 도달하지 못한 경우
  print(-1)

findShortcut()
