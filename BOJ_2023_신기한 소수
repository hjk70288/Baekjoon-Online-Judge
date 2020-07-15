#백준 2023번 신기한 소수
import sys

def is_prime(n): #소수 판별 함수
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if i*i>n:   #루트 n 까지만 판별해 시간복잡도 감소
            break
        if n%i==0:
            return False
    return True
    
n=int(sys.stdin.readline()) #소수의 자릿수
prime=[2,3,5,7] #신기한 소수의 시작 숫자
temp_prime=[] #임시 저장공간

for run in range(n-1): #n-1번 돌면서 n자릿수 소수를 구함
    for i in prime:
        for j in range(1,11,2): #2를 제외한 소수들은 모두 홀수이므로
            if is_prime(int(str(i)+str(j)))==True:  #소수 뒤에 홀수를 더해 그 수가 소수면
                temp_prime.append(int(str(i)+str(j))) #임시 저장공간에 저장
    prime=temp_prime.copy() #임시 저장한 소수들을 신기한 소수의 시작 숫자로 교체
    temp_prime.clear() #임시 저장공간 초기화 후 위 과정을 반복

for i in prime:
    print(i)
