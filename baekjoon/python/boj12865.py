import sys

sys.stdin = open("input.txt", "rt")

if __name__ == "__main__" :
    N, K = map(int, input().split()) ## 물품의 수, 버틸 수 있는 무게

    dp = [0]*(K+1) ## dp[x] : 무게 x에서의 최대의 가치
    for _ in range (N) :
        W, V = map(int, input().split()) ## 물품의 무게, 물품의 가치
        for i in range (K, W-1, -1) : ## 앞에서부터 탐색하게 되면 중복으로 더하는 경우가 생긴다.
            ## (ex) 무게가 2이고 가치가 1인 물건 : (wrong case) 0 0 1 2 3 4 // (good case) 0 0 1 1 1 1
            dp[i] = max(dp[i], dp[i-W] + V)
    print(dp[K])
