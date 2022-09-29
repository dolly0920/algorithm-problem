import sys
from itertools import combinations
from collections import deque

sys.stdin = open("input.txt", "rt")

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def solve(combination) :
    distance = 0

    visited = [[0]*N for _ in range (N)]
    q = deque()
    for r,c in combination :
        visited[r][c] = 1
        q.append((r,c, 0))

    while q :
        x, y, cur = q.popleft()
        for i in range (4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                continue
            if visited[nx][ny] == 1 :
                continue
            visited[nx][ny] = 1 ## 방문 체크
            if city[nx][ny] == 1 : ## 집인 경우
                distance += cur + 1
            q.append((nx, ny, cur+1)) ## 이동

    return distance


if __name__ == "__main__" :
    N, M = map(int,input().split())
    city = []
    for _ in range (N) :
        city.append(list(map(int,input().split())))

    house = []
    chicken = []
    for i in range (N) :
        for j in range (N) :
            if city[i][j] == 2 :
                chicken.append((i,j))

    answer = sys.maxsize
    for chicken_combination in list(combinations(chicken, M)) :
        answer = min(answer, solve(chicken_combination))
    print(answer)
