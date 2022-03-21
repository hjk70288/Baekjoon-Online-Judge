# 게리맨더링 2
import sys

# 데이터 입력
n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 선거구를 나눈 후 각 영역의 크기를 구하기
def divideArea(x, y, d1, d2):
  areaSize = [0 for _ in range(5)]

  # 경계선 긋기
  for i in range(0, d1 + 1):
    area[x + i][y - i] = 5
  for i in range(0, d2 + 1):
      area[x + i][y + i] = 5
  for i in range(0, d2 + 1):
    area[x + d1 + i][y - d1 + i] = 5
  for i in range(0, d1 + 1):
    area[x + d2 + i][y + d2 - i] = 5

  # 1번 구역 칠하기
  for i in range(0, x + d1):
    for j in range(0, y + 1):
      if area[i][j] == 5:
        break
      area[i][j] = 1
      areaSize[0] += matrix[i][j]
  # 2번 구역 칠하기 (뒤에서부터 칠함)
  for i in range(0, x + d2 + 1):
    for j in range(n-1, y, -1):
      if area[i][j] == 5:
        break
      area[i][j] = 2
      areaSize[1] += matrix[i][j]
  # 3번 구역 칠하기
  for i in range(x + d1, n):
    for j in range(0, y - d1 + d2):
      if area[i][j] == 5:
        break
      area[i][j] = 3
      areaSize[2] += matrix[i][j]
  # 4번 구역 칠하기 (뒤에서부터 칠함)
  for i in range(x + d2 + 1, n):
    for j in range(n - 1, y - d1 + d2 - 1, -1):
      if area[i][j] == 5:
        break
      area[i][j] = 4
      areaSize[3] += matrix[i][j]
  # 5번 구역의 크기 구하기
  for i in range(n):
    for j in range(n):
      if area[i][j] == 9 or area[i][j] == 5:
        areaSize[4] += matrix[i][j]

  return max(areaSize) - min(areaSize)
    

result = sys.maxsize
# x, y, d1, d2 구하기
for x in range(n):
  for y in range(n):
    for d1 in range(1, n):
      for d2 in range(1, n):
        if x + d1 + d2 < n and 0 <= y - d1 and y + d2 < n:
          area = [[9 for _ in range(n)] for _ in range(n)]
          minValue = divideArea(x, y, d1, d2)
          if minValue < result:
            result = minValue
print(result)