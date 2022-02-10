# 구슬 탈출 2
import sys
from collections import deque

# 데이터 입력
n, m = map(int, sys.stdin.readline().split(' '))
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = []

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs
def bfs(rx, ry, bx, by):
  depth = 1 # 구슬 이동 횟수
  queue = deque()
  queue.append((rx, ry, bx, by, depth))
  visited.append((rx, ry, bx, by))

  while(queue):
    visit_rx, visit_ry, visit_bx, visit_by, depth = queue.popleft()

    if depth > 10:
      break

    # 상 우 하 좌 시계방향 이동
    for d in range(4):
      next_rx, next_ry, next_bx, next_by = visit_rx, visit_ry, visit_bx, visit_by

      # 이동할 수 있는 한계까지 이동한 구슬의 좌표를 구하기 (R)
      while(1):
        if board[next_rx + dx[d]][next_ry + dy[d]] != '#':
          if board[next_rx + dx[d]][next_ry + dy[d]] == 'O':
            next_rx += dx[d]
            next_ry += dy[d]
            break
          next_rx += dx[d]
          next_ry += dy[d]
        else:
          break
    
      # 이동할 수 있는 한계까지 이동한 구슬의 좌표를 구하기 (B)
      while(1):
        if board[next_bx + dx[d]][next_by + dy[d]] != '#':
          if board[next_bx + dx[d]][next_by + dy[d]] == 'O':
            next_bx += dx[d]
            next_by += dy[d]
            break
          next_bx += dx[d]
          next_by += dy[d]
        else:
          break

      # 파란구슬이 들어간 경우이므로 continue
      if board[next_bx][next_by] == 'O':
        continue

      # 빨간 구슬 하나만 잘 들어간 경우
      if board[next_rx][next_ry] == 'O' and board[next_bx][next_by] != 'O':
        print(depth)
        return
      
      # 구슬들의 위치가 겹치는 경우
      if next_rx == next_bx and next_ry == next_by:
        # 방향전환 전 구슬의 X 좌표 차이값
        x_diff = abs(visit_rx - visit_bx)

        # X좌표 차이값이 0 이상이라면 구슬이 X축 방향으로 이동한 것이므로
        if x_diff > 0:
          # 더 많은 좌표를 이동한 구슬을 한칸 뒤로 옮김
          if abs(visit_rx - next_rx) < abs(visit_bx - next_bx):
            next_bx -= dx[d]
          else:
            next_rx -= dx[d]
        else:
          if abs(visit_ry - next_ry) < abs(visit_by - next_by):
            next_by -= dy[d]
          else:
            next_ry -= dy[d]

      # 구슬들이 처음 방문한 좌표인 경우
      if (next_rx, next_ry, next_bx, next_by) not in visited:
        visited.append((next_rx, next_ry, next_bx, next_by))
        queue.append((next_rx, next_ry, next_bx, next_by, depth + 1))
  print(-1)

# 구슬 위치 찾기
for i in range(n):
  for j in range(m):
    if board[i][j] == 'R':
      rx = i
      ry = j
    if board[i][j] == 'B':
      bx = i
      by = j

bfs(rx, ry, bx, by)