import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def BFS(r, c) :
    q = deque()

    visited[r][c] = 1
    q.append((r,c))
    area = 1

    while q :
        r, c = q.popleft()
        for i in range (4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= M or nc < 0 or nc >= N :
                continue
            if visited[nr][nc] == 1 or paper[nr][nc] != 0 :
                continue
            area += 1
            visited[nr][nc] = 1
            q.append((nr, nc))
    return area


def fill(r1, c1, r2, c2) : ## 0 2 4 4 -> (0,2) => (2,0), (4,4) => (2,3)
    for i in range (r2, r1+1) :
        for j in range (c1, c2+1) :
            paper[i][j] = 1

if __name__ == "__main__" :
    M,N,K = map(int, input().split())

    paper = [[0]*(N) for _ in range (M)]
    visited = [[0]*(N) for _ in range (M)]

    for _ in range (K) :
        x1, y1, x2, y2 = map(int, input().split()) ## (0,2), (4,4) => 사각형 좌표 : (2,0), (2,3)
        fill(M - y1 - 1, x1, M - y2, x2 - 1)

    answer = 0
    areas = []
    for i in range (M) :
        for j in range (N) :
            if visited[i][j] == 0 and paper[i][j] == 0 :
                answer += 1
                areas.append(BFS(i,j))
    print(answer)

    areas.sort()
    print(' '.join(map(str, areas)))