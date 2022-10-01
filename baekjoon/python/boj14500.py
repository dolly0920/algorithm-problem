import sys

sys.stdin = open("input.txt", "rt")

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def DFS(r, c, depth, s) :
    global answer
    if depth == 4 :
        answer = max(answer, s)
        return

    for i in range (4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] == 1 :
            continue
        visited[nr][nc] = 1
        DFS(nr, nc, depth+1, s+paper[nr][nc])
        visited[nr][nc] = 0
    return


if __name__ == "__main__" :
    N, M = map(int, input().split())
    paper = []

    answer = -1
    visited = [[0] * M for _ in range(N)]
    for _ in range (N) :
        paper.append(list(map(int, input().split())))

    for i in range (N) :
        for j in range (M) :
            visited[i][j] = 1
            DFS(i, j, 1, paper[i][j])
            visited[i][j] = 0

            ## 끝점
            if (i == 0 and j == 0) or (i == 0 and j == M-1) or (i == N-1 and j == 0) or (i == N-1 and j == M-1) :
                continue

            if i == 0 : ## ㅜ
                answer = max(answer, paper[i][j] + paper[i][j-1] + paper[i][j+1] + paper[i+1][j])
            elif i == N-1 : ## ㅗ
                answer = max(answer, paper[i][j] + paper[i][j-1] + paper[i][j+1] + paper[i-1][j])
            elif j == 0 : ## ㅏ
                answer = max(answer, paper[i][j] + paper[i-1][j] + paper[i+1][j] + paper[i][j+1])
            elif j == M-1 : ## ㅓ
                answer = max(answer, paper[i][j] + paper[i-1][j] + paper[i+1][j] + paper[i][j-1])
            else :
                temp = paper[i][j] + paper[i-1][j] + paper[i+1][j] + paper[i][j-1] + paper[i][j+1]
                for k in range (4) :
                    ni = i + dr[k]
                    nj = j + dc[k]
                    answer = max(answer, temp-paper[ni][nj])
    print(answer)
