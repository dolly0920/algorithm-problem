import sys

sys.stdin = open("../input.txt", "rt")

## 통과
def solution(n, s, a, b, fares):

    INF = sys.maxsize
    dp = [[INF]*n for _ in range (n)] ## dp[x][y] : x-y 최소 거리
    for i in range (n) :
        dp[i][i] = 0 ## 자기 자신

    ## 운임요금
    for start, end, fare in fares :
        dp[start-1][end-1] = fare
        dp[end-1][start-1] = fare

    ## 플루이드-와샬
    for k in range (n) : ## 거치는 점
        for i in range (n) :
            for j in range (n) :
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    answer = dp[s-1][a-1] + dp[s-1][b-1] ## 동승을 하지 않고 그냥 따로 가는 경우
    ## 특정 지점까지 동승하고 각자 목적지로 향하는 경우
    for i in range (n) :
        answer = min(answer, dp[s-1][i] + dp[i][a-1] + dp[i][b-1])

    return answer

if __name__ == "__main__" :
    n, s, a, b = map(int, input().split())
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, fares))