import sys
from collections import deque

def bfs(x,y):  #빈 공간 탐색을 위한 bfs
    cnt=1      #공간의 넓이 (빈칸의 개수)
    d=deque()      #dfs를 위한 큐 생성
    d.append((x,y))
    visited[x][y]=1    #방문한 곳은 1로
    while d:       #큐가 빌때까지
        x,y=d.popleft()   #선입선출
        for k in range(4): #상 하 좌 우 4방향 검사
            i=x+nx[k]
            j=y+ny[k]
            if i<0 or i>=m or j<0 or j>=n or visited[i][j]==1 or area[i][j]==0:
                continue   #좌표가 배열을 벗어나거나 이미 방문 혹은 빈 공간이 아니면 돌아감
            d.append((i,j))  #검사할 좌표를 큐에 삽입
            visited[i][j]=1  #방문
            cnt+=1    #빈 공간 카운트
    return cnt

m,n,k=map(int,sys.stdin.readline().split())
area=[[1 for i in range(n)] for i in range(m)]    #공간 저장 배열
visited=[[0 for i in range(n)] for i in range(m)]  #방문 확인 배열
resultArr=[]    #결과값 저장
areaCount=0    #덩어리 수 카운트
nx=[-1,1,0,0]  #상하좌우
ny=[0,0,-1,1] 

for i in range(k): 
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            area[i][j]=0     #벽을 0으로 채우기

for i in range(m):     
    for j in range(n):
        if area[i][j]==1 and visited[i][j]!=1: #빈공간이면서 방문을 안했다면
            resultArr.append(bfs(i,j))  #이어진 공간까지 모두 탐색
            areaCount+=1     #덩어리 수 증가

print(areaCount)

resultArr.sort()
for i in resultArr:
    print(i,end=' ')
