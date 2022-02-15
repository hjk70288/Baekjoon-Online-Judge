# 인구 이동
import sys
from collections import deque

# 데이터 입력
n, l, r = map(int, sys.stdin.readline().split(' '))
land = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs로 나라 상우하좌의 국경선이 열렸는지 판단 후 인구 이동
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  people_count = land[x][y] # 연합들 간 인구수의 합
  close_lands = [(x, y)] # 연합(나라) 개수
  is_open = False # 국경선이 열린 곳이 있는지 판단

  while queue:
    visit_x, visit_y = queue.popleft()
    
    for d in range(4):
      next_x = visit_x + dx[d]
      next_y = visit_y + dy[d]

      if next_x < n and next_x != -1 and next_y < n and next_y != -1:
        if visited[next_x][next_y] == False: # 방문하지 않은 나라이면
          # 인구수의 차이가 l 이상 r 이하인지 검사
          people_diff = abs(land[visit_x][visit_y] - land[next_x][next_y])
          if people_diff >= l and people_diff <= r:
            # 나라 방문 처리 후 연합에 추가
            visited[next_x][next_y] = True
            people_count += land[next_x][next_y]
            queue.append((next_x, next_y))
            close_lands.append((next_x, next_y))
            is_open = True
  # 더 이상 방문할 수 있는 나라가 없으면 연합의 인구수 평균으로 인구 이동
  people_count_avg = int(people_count / len(close_lands))
  for close_x, close_y in close_lands:
    land[close_x][close_y] = people_count_avg
  return is_open


duration = 0 # 인구 이동에 걸린 기간

# 국경선이 열린 곳이 하나도 존재하지 않을 때 까지 반복
while True:
  is_open = False # 국경선이 열린 곳이 존재하는지 여부
  visited = [[False for _ in range(n)] for _ in range(n)] # 방문한 나라 정보 초기화

  # 인구 이동
  for i in range(n):
    for j in range(n):
      if visited[i][j] == False:
        tmp_is_open = bfs(i, j)
        if is_open == False:
          is_open = tmp_is_open

  # 국경선이 열린 곳이 하나도 없다면 결과  출력
  if is_open == False:
    print(duration)
    break

  duration += 1