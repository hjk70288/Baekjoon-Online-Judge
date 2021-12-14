# 단지번호 붙이기

def dfs(matrix,x,y,n): #깊이 우선 탐색
    global danji
    danji+=1  #집 수 증가
    mapArr[x][y]=0  #검사한 집은 0으로
    if x-1>=0 and mapArr[x-1][y]==1:  #상
        dfs(mapArr,x-1,y,n)
    if x+1<n and mapArr[x+1][y]==1:  #하
        dfs(mapArr,x+1,y,n)
    if y-1>=0 and mapArr[x][y-1]==1:  #좌
        dfs(mapArr,x,y-1,n)
    if y+1<n and mapArr[x][y+1]==1:  #우
        dfs(mapArr,x,y+1,n)
    return danji  #집 수 리턴

n=int(input()) #지도의 크기
mapArr=[]  #지도의 정보를 담을 리스트
cnt=0      #단지 수
danji=0   #단지안의 집 수
danjiArr=[] #집 수를 오름차순으로 정렬하기위해 여기에 저장
for i in range(n):
    mapArr.append(list(map(int,input())))
for i in range(n):
    for j in range(n):
        if mapArr[i][j]!=0:   #0이면 검사 안함
            danjiArr.append(dfs(mapArr,i,j,n))  #dfs로 탐색후
            danji=0                             #단지안의 집 수 리턴
            cnt+=1   #단지 수 증가
print(cnt)
danjiArr.sort() #집 수 오름차순 정렬
for i in danjiArr:
    print(i)
