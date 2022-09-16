## https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    dp = [[0 for _ in range (m+1)] for _ in range (n+1)] ## dp[i][j] : (i,j)에 도달할 수 있는 최소 가짓 수

    dp[1][1] = 1 ## 시작
    for i in range (1, n+1) :
        for j in range (1, m+1) :
            if i == 1 and j == 1 : continue ## 시작
            if [j,i] in puddles : ## 웅덩이
                dp[i][j] = 0
            else : ## 다른 곳
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[n][m]