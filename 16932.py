# 모양 만들기
import sys
from collections import deque

# 데이터 입력
n, m = map(int, sys.stdin.readline().split(' '))
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 방문 정보 ([방문 여부, 구역 번호])
visited = [[[False, 0] for _ in range(m)] for _ in range(n)]

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs (해당 구역의 크기를 구함)
def dfs(x, y, div_number):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = [True, div_number]
  div_length = 1
  while(queue):
    visit_x, visit_y = queue.popleft()
    for p in range(4):
      if visit_x + dx[p] != -1 and visit_x + dx[p] < n and visit_y + dy[p] != -1 and visit_y + dy[p] < m:
        if not visited[visit_x + dx[p]][visit_y + dy[p]][0] and matrix[visit_x + dx[p]][visit_y + dy[p]] == 1:
          div_length += 1
          matrix[visit_x + dx[p]][visit_y + dy[p]] = div_length
          visited[visit_x + dx[p]][visit_y + dy[p]] = [True, div_number]
          queue.append((visit_x + dx[p], visit_y + dy[p]))
  return div_length

div_number = 1 # 구역 번호
div_length_list = {} # 구역별 크기 모음
# 구역별 크기를 구함
for i in range(n):
  for j in range(m):
    if matrix[i][j] == 1:
        div_length = dfs(i, j, div_number)
        div_length_list[div_number] = div_length
        div_number += 1

''' 
  0인 곳에서 상하좌우로 방문하지 않은 구역이 존재하는지 확인 후
  방문하지 않은 구역의 크기를 더해 구역의 최대 크기를 구함
'''
result = 0 # 결과 값
for i in range(n):
  for j in range(m):
    if matrix[i][j] == 0:
      div_max_length = 1 # 구역의 최대 크기
      visited_div = [] # 방문한 구역
      for p in range(4):
        if i + dx[p] != -1 and i + dx[p] < n and j + dy[p] != -1 and j + dy[p] < m:
          if visited[i + dx[p]][j + dy[p]][1] not in visited_div and (visited[i + dx[p]][j + dy[p]][1] != 0):
            visited_div.append(visited[i + dx[p]][j + dy[p]][1]) # 해당 구역 방문 처리
            div_max_length += div_length_list[visited[i + dx[p]][j + dy[p]][1]] # 해당 구역의 크기를 최대 크기에 더함
      if div_max_length > result:
        result = div_max_length
print(result)