# 로봇청소기
import sys

def solve(x,y,d):
    cnt=1 #청소한 방의 수
    clean[x][y]=1  #청소했으면 1
    while True:
        flag=0   #청소기가 벽이나 청소한 구역으로 둘러싸여있는지 확인하기 위한 플래그
        if d<0:  # 0 1 2 3 에서 벗어나지 않음
            d=3
        tempDir=d   #현재 방향의 뒤쪽 방향을 이용하기위한 변수
        if clean[x-1][y]!=1 and room[x-1][y]!=1:  
            flag=1
        if clean[x+1][y]!=1 and room[x+1][y]!=1:
            flag=1                                  #사면중 청소할 곳이 한곳이라도 있으면 플래그는 1
        if clean[x][y-1]!=1 and room[x][y-1]!=1:
            flag=1
        if clean[x][y+1]!=1 and room[x][y+1]!=1:
            flag=1
        if flag==0:            #사면중 청소할 곳이 없다면
            tempDir-=1       # -1을 함으로써 현재방향 뒤쪽을 검사 (서쪽의 서쪽은 반대편)
            if tempDir<0:    # 0 1 2 3 에서 벗어나지 않음
                tempDir=3
            if room[x+nx[tempDir]][y+ny[tempDir]]==1:  #현재 방향 뒤 또한 벽으로 둘러싸여있다면
                return cnt     
            else:    
                x,y=x+nx[tempDir],y+ny[tempDir]     #뒤쪽으로 탈출 가능이면  (벽이아님)
                continue
        i=x+nx[d]      #현재 방향의 서쪽검사
        j=y+ny[d] 
        if clean[i][j]==1 or room[i][j]==1:   #벽이있거나 이미 청소했다면
            d-=1    #방향 전환
            continue
        clean[i][j]=1   #청소 가능 구역이므로 청소함
        d-=1      #청소를 했어도 방향은 전환함
        x,y=i,j   #현재 좌표 갱신
        cnt+=1    #청소한 방의 수 증가

n,m=map(int,sys.stdin.readline().split()) 
room=[]*n   #벽의 위치를 저장할 배열
clean=[[0 for i in range(m)] for i in range(n)]  #청소한 구역의 위치를 저장할 배열
r,c,d=map(int,sys.stdin.readline().split()) 
for i in range(n):                                         
    room.append(list(map(int,sys.stdin.readline().split())))
nx=[0,-1,0,1]                 #     북            0
ny=[-1,0,1,0]                 #   서  동        3   1
                              #     남            2
print(solve(r,c,d))
