# 토마토
import sys
from collections import deque

# 열, 행
M, N = list(map(int, sys.stdin.readline().split(' ')))

tomato = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
queue = deque()

# 상, 우, 하, 좌 (시계방향)
x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]

# 익은 곳 위치 저장
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

# queue를 사용하여 bfs
while(queue):
    visit_point = queue.popleft()
    for p in range(4):
        if visit_point[0] + x[p] != -1 and visit_point[0] + x[p] < N and visit_point[1] + y[p] != -1 and visit_point[1] + y[p] < M:
            if tomato[visit_point[0] + x[p]][visit_point[1] + y[p]] == 0:
                tomato[visit_point[0] + x[p]][visit_point[1] + y[p]] = tomato[visit_point[0]][visit_point[1]] + 1
                queue.append((visit_point[0] + x[p], visit_point[1] + y[p]))

result = 0
# 결과 행 순환
for i in tomato:
    # 행에 0인 값이 존재하는 경우는 토마토를 모두 익힐 수 없는 경우
    if 0 in i:
        print(-1)
        exit(0)
    # 해당 행의 최대값과 현재 결과 값을 비교하여 큰 값을 결과 값으로 저장
    result = max(result, max(i))

print(result - 1)