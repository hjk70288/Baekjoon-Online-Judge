# 쉬운 계단 수
dp=[[0 for i in range(10)] for i in range(101)] 
for i in range(1,10):   #dp[i][j] i자릿수의 j로 시작하는 계단 수의 개수
    dp[1][i]=1    #한자리 계단 수는 1~9 자기자신 하나이다
dp[0][1]=1
for i in range(2,101):   
    dp[i-1][0]=dp[i-2][1]   #두번째 자릿수가 0으로 시작할때 세번째 자릿수는 무조건 1이다
    for j in range(1,10):   #따라서 두번째 자릿수가 0인 계단수는 세번째 자릿수가 1인 계단수와 같다
        if j==9:   #첫째 자리가 9면 둘째 자리 숫자는 무조건 8이다
            dp[i][j]=dp[i-1][8]%1000000000
        else:      #i자리 j로 시작하는 계단 수 = 자릿수가 i-1인 j-1, j+1로 시작하는 계단수의 합
            dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%1000000000

n=int(input())
print(sum(dp[n][1:10]) % 1000000000) #길이가 n인 계단수의 개수 출력

#45656이란 수를 보자.
#이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.