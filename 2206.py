# 벽 부수고 이동하기
import sys
from collections import deque

# 데이터 입력
n, m = map(int, sys.stdin.readline().split(' '))
matrix = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
queue = deque()

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 탐색으로 최단 경로 찾기
def findShortcut():
  queue.append((0, 0, 1))
  visited = [[['False' for _ in range(2)] for _ in range(m)] for _ in range(n)]
  visited[0][0] = [0, 0]

  while queue:
    visitX, visitY, crashable = queue.popleft()

    if visitX + 1 == n and visitY + 1 == m:
      print(visited[visitX][visitY][crashable] + 1)
      return 0

    for d in range(4):
      nextX, nextY = visitX + dx[d], visitY + dy[d]

      '''
        벽을 아예 부수지 않고 진행하는 경우와 벽을 만났을 때 벽을 부술 수 있다면 부수는 경우 모두를 큐에 넣고 진행
        각 경우에 대해 따로따로 완전 탐색이 된다
      '''

      # 경계를 넘지 않고
      if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
        # 이동할 수 있는 공간인 경우
        if matrix[nextX][nextY] == 0:
          if visited[nextX][nextY][crashable] == 'False':
            visited[nextX][nextY][crashable] = visited[visitX][visitY][crashable] + 1
            queue.append((nextX, nextY, crashable))
        # 벽인 경우
        else:
          # 벽을 부술 수 있다면
          if crashable > 0:
            if visited[nextX][nextY][crashable - 1] == 'False':
              visited[nextX][nextY][crashable - 1] = visited[visitX][visitY][crashable] + 1
              queue.append((nextX, nextY, crashable - 1))
  print(-1)

findShortcut()