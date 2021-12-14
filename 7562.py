# 나이트의 이동
import sys
from collections import deque

# 나이트가 이동할 수 있는 방향
x = [-2, -1, 1, 2, -2, -1, 1, 2]
y = [-1, -2, -2, -1, 1, 2, 2, 1]

# 테스트 케이스 수
N = int(sys.stdin.readline())

for _ in range(N):
    # 체스판의 크기
    I = int(sys.stdin.readline())
    queue = deque()
    board = [[0 for _ in range(I)] for _ in range(I)]

    # 출발 지점
    start_x, start_y = map(int, sys.stdin.readline().split(' '))
    board[start_x][start_y] = 1

    # 도착 지점
    finish_x, finish_y = map(int, sys.stdin.readline().split(' '))

    # 출발 지점과 도착 지점이 같은 경우 0 출력 후 종료
    if(start_x == finish_x and start_y == finish_y):
        print(0)
        continue

    # bfs를 이용하여 최단거리 탐색
    queue.append((start_x, start_y))
    while(queue):
        visit_x, visit_y = queue.popleft()
        # 목표 칸인 경우 결과 출력 후 탐색 종료
        if visit_x == finish_x and visit_y == finish_y:
            print(board[visit_x][visit_y] - 1)
            break
        for i in range(8):
            if (-1 < visit_x + x[i] < I) and (-1 < visit_y + y[i] < I):
                # 방문하지 않은 칸인 경우 큐에 인접 노드(나이트가 이동할 수 있는 방향)들의 좌표 삽입
                if board[visit_x + x[i]][visit_y + y[i]] == 0:
                    queue.append((visit_x + x[i], visit_y + y[i]))
                    board[visit_x + x[i]][visit_y + y[i]] = board[visit_x][visit_y] + 1