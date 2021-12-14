# 스타트와 링크
import sys

# 데이터 입력
N = int(sys.stdin.readline())  # 인원 수
status = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]  # 능력치

# 팀이 생성될 수 있는 모든 경우의 수(순열)를 구함
visit = [0 for _ in range(N)]
stack = []
case_of_team = []
def solve(prev_number):
    if len(stack) == N // 2:
        case_of_team.append(stack.copy())
    for i in range(N):
        if visit[i] == 0 and i >= prev_number:
            stack.append(i)
            visit[i] = 1
            solve(i)
            stack.pop()
            visit[i] = 0
solve(0)

# 스타트팀, 링크팀의 능력치 차이의 최소 값을 구해야하므로 결과 값을 한계 값으로 초기화
result = sys.maxsize

# 팀이 이뤄질 수 있는 모든 경우의 수를 순환
# 스타트팀은 순열의 시작, 링크팀은 순열의 마지막으로 설정하면 짝이 맞게됨
for n in range(len(case_of_team) // 2):
    start_team = case_of_team[n]
    start_team_ststus = 0
    link_team = case_of_team[-n - 1]
    link_team_status = 0

    # 스타트팀의 능력치 값 구하기
    for i in start_team:
        for j in start_team:
            start_team_ststus += status[i][j]

    # 링크팀의 능력치 값 구하기
    for i in link_team:
        for j in link_team:
            link_team_status += status[i][j]

    # 두 팀의 능력치 차이의 절대값
    status_diff = abs(start_team_ststus - link_team_status)

    # 결과 값과 비교해서 최소값 구하기
    result = min(result, status_diff)

print(result)