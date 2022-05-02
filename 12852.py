# 1로 만들기 2
import sys

# 데이터 입력
x = int(sys.stdin.readline())
dp= [0 for _ in range(1000001)] # i 숫자를 만들기 위해 소요되는 최소 횟수 저장
history= [0 for _ in range(1000001)] # i 숫자에서 3가지 연산 중 최적의 연산을 한 경우의 숫자
dp[1] = 0

# 숫자 2 부터 소요되는 최소 횟수 구하기
for i in range(2, x + 1):
  # 1을 빼는 연산을 우선 적용함
  dp[i] = dp[i - 1] + 1
  history[i] = i - 1

  # 3으로 나누는 연산이 가능한 경우
  if i % 3 == 0:
    # 3으로 나눈 연산을 적용했을 때의 소요 횟수가 더 적다면
    if dp[i] > dp[int(i / 3)] + 1:
        history[i] = int(i / 3) # 최적의 연산을 한 경우 이므로 기록 저장
    dp[i] = min(dp[i], dp[int(i / 3)] + 1)
  # 위의 3으로 나누는 연산과 동일한 로직
  if i % 2 == 0:
    if dp[i] > dp[int(i / 2)] + 1:
        history[i] = int(i / 2)
    dp[i] = min(dp[i], dp[int(i / 2)] + 1)

# 결과 출력
if x == 1:
  print(0)
  print(1)
else:
  resultNumber = x
  print(dp[resultNumber])
  print(x, end = ' ')
  while True:
    print(history[resultNumber], end = ' ')
    resultNumber = history[resultNumber]
    if (resultNumber == 1):
      break