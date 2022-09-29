import sys
from collections import deque
from copy import deepcopy

sys.stdin = open("input.txt", "rt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

def getSafeZone(N, M, arr) :
    global answer
    visited = [[0]*M for _ in range (N)]

    for x, y in virus :
        visited[x][y] = 1

    q = deepcopy(virus)

    while q :
        x, y = q.popleft()
        for i in range (4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or arr[nx][ny] == 1 or visited[nx][ny] == 1 :
                continue
            visited[nx][ny] = 1
            q.append((nx, ny))

    count = 0
    for i in range (N) :
        for j in range (M) :
            if arr[i][j] == 0 and visited[i][j] == 0:
                count += 1

    answer = max(answer, count)
    return count



def solve(N, M, arr, index, depth) :
    if index >= N*M :
        return

    if depth == 3 :
        getSafeZone(N, M, arr)
        return

    row = index // M
    col = index % M

    if arr[row][col] == 0: ## 빈칸인 경우
        arr[row][col] = 1 ## 벽 세우기
        solve(N, M, arr, index+1, depth+1)
        arr[row][col] = 0 ## 벽 허물기
    solve(N, M, arr, index+1, depth)

if __name__ == "__main__" :
    N,M = map(int, input().split())
    arr = []
    for _ in range (N) :
        arr.append(list(map(int, input().split())))

    virus = deque()
    for i in range (N) :
        for j in range (M) :
            if arr[i][j] == 2 : ## 바이러스
                virus.append((i,j))

    solve(N, M, arr, 0, 0)
    print(answer)

