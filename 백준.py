import sys
import heapq
n=int(sys.stdin.readline())
maxHeapArr=[]
minHeapArr=[]
maxLen=0
minLen=0
'''
def maxHeap(n):
    global maxLen
    maxHeapArr.append(n)
    maxLen+=1
    for i in range(1,maxLen):
        while(1):
            if i==1:
                break
            if i!=1 and maxHeapArr[i]>maxHeapArr[i//2]:
                tmp=maxHeapArr[i]
                maxHeapArr[i]=maxHeapArr[i//2]
                maxHeapArr[i//2]=tmp
            i=i//2

def minHeap(n):
    global minLen
    minHeapArr.append(n)
    minLen+=1
    for i in range(1,minLen):
        while(1):
            if i==1:
                break
            if i!=1 and minHeapArr[i]<minHeapArr[i//2]:
                tmp=minHeapArr[i]
                minHeapArr[i]=minHeapArr[i//2]
                minHeapArr[i//2]=tmp
            i=i//2
'''
#maxHeap(int(sys.stdin.readline()))
tmpNum=int(sys.stdin.readline())
heapq.heappush(maxHeapArr,(tmpNum*-1,tmpNum))
maxLen+=1
print(maxHeapArr[0][1])
for i in range(n-1):
    num=int(sys.stdin.readline())
    if maxLen==minLen:
        if minHeapArr[0]<=num:
            temp=minHeapArr[0]
            heapq.heappop(minHeapArr)
            minLen-=1
            #minHeap(num)
            heapq.heappush(minHeapArr,num)
            minLen+=1
            num=temp
        #maxHeap(num)
        heapq.heappush(maxHeapArr,(num*-1,num))
        maxLen+=1
    else:
        if maxHeapArr[0][1]>num:
            temp=maxHeapArr[0][1]
            heapq.heappop(maxHeapArr)
            maxLen-=1
            #maxHeap(num)
            heapq.heappush(maxHeapArr,(num*-1,num))
            maxLen+=1
            num=temp
        #minHeap(num)
        heapq.heappush(minHeapArr,num)
        minLen+=1
    
    print(maxHeapArr[0][1])