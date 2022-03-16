# 경사로
import sys

# 데이터 입력
N, L = map(int, sys.stdin.readline().split(' '))
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
flipMatrix = list(map(list, zip(*matrix))) # 기존 데이터에서 행과 열이 뒤집힌 배열
resultRoadCount = 0 # 이용 가능한 길의 개수 결과

# 이용 가능한 길의 개수를 구함
def countAvailableRoad(matrix):
  roadCount = 0 # 이용 가능한 길의 개수
  ramp = [[False for _ in range(N)] for _ in range(N)] # 경사로 설치 여부

  for i in range(N):
    breakFlag = False
    prevHeight = matrix[i][0] # 이전 영역의 높이
    for j in range(1, N):
      curHeight = matrix[i][j] # 현재 영역의 높이

      # 높이의 차이가 1보다 큰 경우
      if abs(prevHeight - curHeight) > 1:
        breakFlag = True

      # 높이의 차이가 작아진 경우
      elif prevHeight - curHeight == 1:
        # 해당 영역부터 L의 크기만큼 앞으로 검사
        for l in range(j, j + L):
          if l >= N or matrix[i][l] != curHeight: # 높이가 다른 영역이 있다면 경사로 설치 불가
            breakFlag = True
            break

        # 경사로 설치 정보 갱신
        if breakFlag == False:
          for l in range(j, j + L):
            ramp[i][l] = True
        
      # 높이의 차이가 커진 경우
      elif prevHeight - curHeight == -1:
        # 이전 영역부터 L의 크기만큼 뒤로 검사
        for l in range(j - 1, j - 1 - L, -1):
          if l < 0 or matrix[i][l] != prevHeight or ramp[i][l] == True: # 높이가 다른 영역이 있거나 이미 경사로가 설치되어 있는 경우 설치 불가
            breakFlag = True
            break

        # 경사로 설치 정보 갱신
        if breakFlag == False:
          for l in range(j - 1, j - 1 - L, -1):
            ramp[i][l] = True

      prevHeight = curHeight # 이전 높이 값 갱신
      
      if breakFlag:
        break

      if j == N - 1:
        roadCount += 1

  return roadCount

resultRoadCount += countAvailableRoad(matrix)
resultRoadCount += countAvailableRoad(flipMatrix)
print(resultRoadCount)