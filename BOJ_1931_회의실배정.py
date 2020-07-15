import sys
n=int(sys.stdin.readline())
meeting=[]  #회의의 시작, 종료 시간을 저장할 리스트
for i in range(n):  #데이터 입력
    meeting.append(list(map(int,sys.stdin.readline().split())))
meeting.sort(key=lambda x:(x[1],x[0]))  #회의가 끝나는 시간을 기준으로 정렬한 후 그 안에서 시작 시간을 기준으로 한번 더 정렬(오름차순)
maxMeet=1  #최댓값을 저장할 변수(자기 자신 포함 초기값 1)
start=meeting[0][1]  #시작을 0행 1열(끝나는 시간)로 설정
for i in range(1,n):   #1부터 n-1까지 반복
    if start<=meeting[i][0]: #끝나는 시간보다 다음행의 시작 시간이 더 늦는다면
        maxMeet+=1  #최댓값 카운트
        start=meeting[i][1]  #시작을 다음행 끝나는 시간으로 설정
print(maxMeet)  #출력
