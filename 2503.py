# 숫자 야구
import sys

# 데이터 입력
n = int(sys.stdin.readline())
baseball = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 유효한 숫자인지 체크 (각 자릿수가 모두 다르며, 1 ~ 9 사이의 숫자로 이루어져야 함)
def checkRightAnswer(answer):
  answer = str(answer)
  if answer[0] == '0' or answer[1] == '0' or answer [2] == '0':
    return False
  elif answer[0] != answer[1] and answer[0] != answer[2] and answer[1] != answer[2]:
    return True
  else:
    return False

result = 0 # 답 개수
for answer in range(123, 988):
  # 유효한 숫자이면
  if(checkRightAnswer(answer)):
    # 해당 숫자와 질문에 대한 답을 비교
    for questionIndex, question in enumerate(baseball):
      # 질문한 답과 그에 따른 스트라이크, 볼 결과
      questionAnswer = question[0]
      questionStrike = question[1]
      questionBall = question[2]

      # 현재 검사중인 숫자의 스트라이크, 볼 결과
      strike = 0
      ball = 0

      # 질문에 대한 답과 현재 검사중인 숫자를 비교하여 스크라이크, 볼 개수 구하기
      for numberIndex, number in enumerate(str(answer)):
        for d in range(3):
          if number == str(questionAnswer)[d]:
            if numberIndex == d:
              strike += 1
            else:
              ball += 1
            break
      # 스크라이트, 볼 개수가 질문에 대한 답과 다르면 검사한 숫자는 정답이 될 수 없음
      if questionStrike != strike or questionBall != ball:
        break

      # 모든 질문에 부합하면 정답이 될 수 있음
      if questionIndex == n - 1:
        result += 1

print(result)