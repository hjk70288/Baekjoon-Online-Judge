# 알파벳
import sys

# 데이터 입력
r, c = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().strip()) for _ in range(r)]

# 상, 우, 하, 좌 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# DFS 탐색 백트래킹
def dfs(x, y, length):
  global minResult

  # 방문한 적이 있는 알파벳이면 탐색 종료
  if visited[ord(matrix[x][y]) - 65] == True:
    if minResult < length:
      minResult = length
    return 0

  for d in range(4):
    nextX, nextY = x + dx[d], y + dy[d]

    # 백트래킹
    if nextX >= 0 and nextX < r and nextY >= 0 and nextY < c:
      alphabetIndex = ord(matrix[x][y]) - 65 # 알파벳을 숫자로 변환 (A: 0, B: 1 ...)
      visited[alphabetIndex] = True
      dfs(nextX, nextY, length + 1)
      visited[alphabetIndex] = False

visited = [False for _ in range(26)]
minResult = 0
dfs(0, 0, 0)
print(minResult)
