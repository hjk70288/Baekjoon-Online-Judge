# 토마토
import sys
from collections import deque

# 열, 행, 높이
M, N ,H = map(int, sys.stdin.readline().split(' '))

# 상, 우, 하, 좌, 위(앞), 아래(뒤)
x = [-1, 0, 1, 0, 0, 0]
y = [0, 1, 0, -1, 0, 0]
z = [0, 0, 0, 0, -1, 1]

# 데이터 입력
tomato = []
queue = deque()
for _ in range(H):
    tomato_temp = []
    for _ in range(N):
        tomato_temp.append(list(map(int, sys.stdin.readline().split())))
    tomato.append(tomato_temp)

# 익은 곳 위치 저장
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k))

# bfs로 토마토 익히기
while(queue):
    visit_z, visit_x, visit_y = queue.popleft()
    for i in range(6):
        if -1 < visit_x + x[i] < N and -1 < visit_y + y[i] < M and -1 < visit_z + z[i] < H and tomato[visit_z + z[i]][visit_x + x[i]][visit_y + y[i]] == 0:
            tomato[visit_z + z[i]][visit_x + x[i]][visit_y + y[i]] = tomato[visit_z][visit_x][visit_y] + 1
            queue.append((visit_z + z[i], visit_x + x[i], visit_y + y[i]))

# 익힌 후 토마토들을 순환
result = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 아직 익지 않은 토마토가 존재하는 경우
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            # 해당 토마토가 익는데 걸리는 시간과 현재 결과 값을 비교하여 큰 값을 결과 값으로 저장
            result = max(tomato[i][j][k], result)
print(result - 1)