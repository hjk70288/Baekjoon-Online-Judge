# 하이퍼 토마토
import sys
from collections import deque

# 창고 크기
m, n, o, p, q, r, s, t, u, v, w = list(map(int, sys.stdin.readline().split(' ')))

# 데이터 입력
tomato = [[[[[[[[[[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]
queue = deque()

# 익은 토마토가 영향을 줄 수 있는 방향 (direction)
dm = [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
do = [0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dp = [0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dq = [0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
dt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0]
du = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0]
dv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0]
dw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1]

# 토마토가 익은 곳의 위치 저장 (index)
for idw in range(w):
    for idv in range(v):
        for idu in range(u):
            for idt in range(t):
                for ids in range(s):
                    for idr in range(r):
                        for idq in range(q):
                            for idp in range(p):
                                for ido in range(o):
                                    for idn in range(n):
                                        for idm in range(m):
                                            if tomato[idw][idv][idu][idt][ids][idr][idq][idp][ido][idn][idm] == 1:
                                                queue.append((idw, idv, idu, idt, ids, idr, idq, idp, ido, idn, idm))

# bfs로 토마토 익히기
while(queue):
    # 방문한 곳의 좌표 (visit)
    vw, vv, vu, vt, vs, vr, vq, vp, vo, vn, vm = queue.popleft()

    # 다음 방문할 좌표 (next)
    for i in range(22):
        nw = vw + dw[i]
        nv = vv + dv[i]
        nu = vu + du[i]
        nt = vt + dt[i]
        ns = vs + ds[i]
        nr = vr + dr[i]
        nq = vq + dq[i]
        np = vp + dp[i]
        no = vo + do[i]
        nn = vn + dn[i]
        nm = vm + dm[i]

        if -1 < nw < w and -1 < nv < v and -1 < nu < u and -1 < nt < t and -1 < ns < s and -1 < nr < r and -1 < nq < q and -1 < np < p and -1 < no < o and -1 < nn < n and -1 < nm < m:
            if tomato[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == 0:
                tomato[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = tomato[vw][vv][vu][vt][vs][vr][vq][vp][vo][vn][vm] + 1
                queue.append((nw, nv, nu, nt, ns, nr, nq, np, no, nn, nm))

# 익히는데 가장 오래걸린 토마토 찾기
result = 0
for idw in range(w):
    for idv in range(v):
        for idu in range(u):
            for idt in range(t):
                for ids in range(s):
                    for idr in range(r):
                        for idq in range(q):
                            for idp in range(p):
                                for ido in range(o):
                                    for idn in range(n):
                                        for idm in range(m):
                                            # 아직도 익지 않은 곳이 있다면 -1 출력 후 종료
                                            if tomato[idw][idv][idu][idt][ids][idr][idq][idp][ido][idn][idm] == 0:
                                                print(-1)
                                                exit(0)
                                            result = max(result, tomato[idw][idv][idu][idt][ids][idr][idq][idp][ido][idn][idm])
print(result - 1)