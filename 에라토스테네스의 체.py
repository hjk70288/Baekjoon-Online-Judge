def prime_list(n):   #n까지의 소수 배열 반환 (소수면 True)
    sieve = [True]*(n+1)  #에라토스테네스의 체 초기화
    for i in range(2,n+1):  #2부터 입력한 수까지 반복
        if sieve[i] == True: #검사한 수가 소수면      
            for j in range(i+i, n, i): #그 수의 배수들을 False로 입력
                sieve[j] = False
    return sieve
