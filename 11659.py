# 구간 합 구하기 4
import sys

# 데이터 입력
n, m = map(int, sys.stdin.readline().split(' '))
numbers = list(map(int, sys.stdin.readline().split(' ')))
prefixSum = [0]

# 누적 합 구하기
preNumber = 0
for number in numbers:
  prefixSum.append(preNumber + number)
  preNumber += number

# 구간 합 출력
for i in range(m):
  startIndex, finIndex = map(int, sys.stdin.readline().split(' '))
  print(prefixSum[finIndex] - prefixSum[startIndex - 1])