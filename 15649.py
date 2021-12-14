# N과 M (1)

# 데이터 입력
N, M = map(int, input().split(' '))

# 방문 여부 (0이면 미방문, 1이면 방문)
visit = [0 for _ in range(N + 1)]

# 방문한 수를 저장할 스택
stack = []

def solve():
    # 만족하는 수열의 길이에 도달하면 출력
    if len(stack) == M:
        print(*stack)
        return
    # 1부터 N까지의 수를 반복
    for i in range(1, N + 1):
        # 해당 수에 방문하지 않은 경우
        if visit[i] == 0:
            # 방문으로 설정하고 스택에 추가
            visit[i] = 1
            stack.append(i)
            solve()
            # 출력 완료 후 미방문으로 설정하고 스택에서 제거
            visit[i] = 0
            stack.pop()

solve()