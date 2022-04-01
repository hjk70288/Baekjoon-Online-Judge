# N-Queen
import sys

# 데이터 입력
n = int(sys.stdin.readline())
resultCase = 0
queenPoint = [] # 퀸이 놓여져있는 좌표

# 퀸을 놓을 수 있는 경우의 수 구하기
def getQueenCase(x):
  global resultCase

  # 마지막 행까지 퀸을 모두 놓은 경우
  if x == n:
    resultCase += 1
    return 0

  # 놓을 수 있는 열 구하기
  for y in range(n):
    canSet = True

    # 같은 열, 대각선 방향에 퀸이 존재하는지 검사
    if len(queenPoint) != 0:
      for queen in queenPoint:
        queenX, queenY = queen[0], queen[1]
        if queenY == y or (abs(queenX - x) == abs(queenY - y)):
          canSet = False
          break

    if canSet: # 해당 열에 퀸을 놓을 수 있으면
      queenPoint.append((x, y)) # 퀸을 놓고
      getQueenCase(x + 1) # 다음 행 검사
      queenPoint.pop() # 해당 열에 대해 검사가 끝난 경우 놓은 퀸을 없앰

getQueenCase(0)
print(resultCase)

# 실패한 코드
'''
import sys
from copy import deepcopy

# 데이터 입력
n = int(sys.stdin.readline())
resultCase = 0
queenPoint = [] # 퀸이 놓여져있는 좌표

# 같은 열, 대각선 방향에 퀸이 존재하는지 검사
def canSetQueen(x, y):
  for queen in queenPoint:
    queenX, queenY = queen[0], queen[1]
    if queenY == y or (abs(queenX - x) == abs(queenY - y)):
      return False
  return True

# 퀸을 놓을 수 있는 경우의 수 구하기
def getQueenCase(x):
  global resultCase

  # 마지막 행까지 퀸을 모두 놓은 경우
  if x == n:
    resultCase += 1
    return 0

  # 놓을 수 있는 열 구하기
  for y in range(n):  
    if canSetQueen(x, y): # 해당 열에 퀸을 놓을 수 있으면
      queenPoint.append((x, y)) # 퀸을 놓고
      getQueenCase(x + 1) # 다음 행 검사
      queenPoint.pop() # 해당 열에 대해 검사가 끝난 경우 놓은 퀸을 없앰

getQueenCase(0)
print(resultCase)
'''