import sys
import copy
from collections import deque

def check(iceberg):
    visited=[[0 for i in range(m)]for i in range(n)]  #방문을 기록하는 배열
    cnt=0 #덩어리
    for i in range(n):
        for j in range(m):
            if iceberg[i][j]!=0 and visited[i][j]!=1: #바다가 아니고 방문을 안했다면
                bfs(iceberg,visited,i,j) 
                cnt+=1
    return cnt

def bfs(iceberg,visited,i,j):
    d=deque()   #bfs를 위한 큐 생성 (좌표를 담아둠)
    d.append((i,j))
    visited[i][j]=1  #방문함 (1)
    while d:
        i,j=d.popleft()
        for c in range(4):  #상하좌우 체크
            x=i+nx[c]
            y=j+ny[c]
            if x<0 or x>=n or y<0 or y>=m or iceberg[x][y]==0 or visited[x][y]==1:continue
            d.append((x,y))
            visited[x][y]=1

def nextYear(iceberg):
    copyIceberg=copy.deepcopy(iceberg)  #copy배열은 현재 빙하 위치를 기역하기 위함
    for i in range(n):
        for j in range(m):
            if copyIceberg[i][j]!=0:  #빙하가 있으면
                cnt=0 #주변 바다 수
                for c in range(4):
                    x=i+nx[c]
                    y=j+ny[c]
                    if x<0 or x>=n or y<0 or y>=m or copyIceberg[x][y]!=0:continue
                    cnt+=1 #상하좌우에 바다가 몇개있는지
                iceberg[i][j]=max(0,iceberg[i][j]-cnt) #음수가되면 0으로 바꾸기 위함

def checkZero(iceberg):
    for i in range(n):
        for j in range(m):
            if iceberg[i][j]!=0:
                return False
    return True

n,m=map(int,input().split())
iceberg=[]  #빙산의 정보 (맵)
nx=[-1,1,0,0]     #상하좌우
ny=[0,0,-1,1] 
year=0  #년도

for i in range(n):   #데이터 입력
    iceberg.append(list(map(int,sys.stdin.readline().strip(' \n').split(' '))))

while(True):
    if check(iceberg)>1:    #덩어리 수가 1개 이상이면 종료
        print(year)
        break
    elif checkZero(iceberg): #모두 녹을때까지 덩어리가 안만들어지면
        print(0)
        break
    nextYear(iceberg)  #다음년도 빙하 만들기
    year+=1  
