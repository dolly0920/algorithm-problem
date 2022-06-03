import sys

sys.stdin = open("input.txt", "rt")

answer = sys.maxsize ## 최소 순회 거리

def dfs(dest, current, order, cost) :
    global answer
    if (cost >= answer) :
        return

    ## 순회
    for next in range (N) :
        if visit[next] == 0 and path[current][next] != 0 :
            visit[next] = 1
            dfs(dest, next, order + 1, cost + path[current][next])
            visit[next] = 0
        elif order + 1 == N and next == dest and path[current][next] != 0:
            answer = min(answer, cost + path[current][next])
            return

if __name__ == "__main__" :
    N = int(input()) ## 도시의 수 N
    visit = [[0 for _ in range (N)] for _ in range (N)]
    path = []
    for _ in range (N) :
        arr = list(map(int,input().split()))
        path.append(arr)
    for start in range (N) :
        visit[start] = 1
        dfs(start, start, 0, 0)
        visit[start] = 0
    print(answer)

