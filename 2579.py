# 계단 오르기
import sys

# 데이터 입력
n = int(sys.stdin.readline())
dp = [0 for _ in range(301)]
stair = [int(sys.stdin.readline()) for _ in range(n)]
dp[0] = stair[0] # 첫 번째 계단까지 오르는 경우 최대값
dp[1] = stair[0] + stair[1] # 두 번째 계단까지 오르는 경우 최대값
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2]) # 세 번째 계단까지 오르는 경우 최대값

# 네 번째 계단부터 dp 시작
for i in range(3, n):
  # dp[i - 2] + stair[i] -> 두 계단씩 오른 경우
  # dp[i - 3] + stair[i - 1] + stair[i] -> 한 계단씩 오른 경우 (세 계단 연속으로 한 계단씩 오를 수 없으므로 세 계단 전에서 두 계단씩 올라야함)
  dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[n - 1])