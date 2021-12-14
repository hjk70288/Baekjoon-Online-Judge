# 가운데를 말해요
#최대힙의 크기(갈이)는 항상 최소힙보다 같거나 1크다

import sys
import heapq  #최대힙 최소힙 구현을 위한 heapq
n=int(sys.stdin.readline())
maxHeapArr=[]    #최대힙
minHeapArr=[]    #최소힙
maxLen=0   #최대힙의 길이
minLen=0   #최소힙의 길이
tempNum=int(sys.stdin.readline()) #맨처음 입력을 최대힙으로 넣는다
heapq.heappush(maxHeapArr,(tempNum*-1,tempNum)) #최대힙에 push
maxLen+=1
print(maxHeapArr[0][1]) #맨처음엔 비교대상이 없으므로 바로 출력
for i in range(n-1): #위에서 이미 한번 push했으므로 n-1번 실행
    num=int(sys.stdin.readline())
    if maxLen==minLen:   #두 힙의 길이가 같을때
        if minHeapArr[0]<=num:  #입력값이 최소힙의 루트보다 크면
            temp=minHeapArr[0]   
            heapq.heappop(minHeapArr) #최소힙의 루트를 pop
            minLen-=1
            heapq.heappush(minHeapArr,num) #최소힙에 입력값을 push
            minLen+=1
            num=temp 
        heapq.heappush(maxHeapArr,(num*-1,num)) #입력값 혹은 최소힙에서 pop한 값을 최대힙에 push
        maxLen+=1
    else:     #두 힙의 길이가 다를때
        if maxHeapArr[0][1]>num:    #입력값이 최대힙의 루트보다 작으면 
            temp=maxHeapArr[0][1]
            heapq.heappop(maxHeapArr)  #최대힙의 루트를 pop
            maxLen-=1      
            heapq.heappush(maxHeapArr,(num*-1,num))  #최대힙에 입력값을 push
            maxLen+=1
            num=temp
        heapq.heappush(minHeapArr,num)     #입력값 혹은 최대힙에서 pop한 값을 최소힙에 push
        minLen+=1  
    print(maxHeapArr[0][1])   #최대힙의 루트가 항상 중간값이다
