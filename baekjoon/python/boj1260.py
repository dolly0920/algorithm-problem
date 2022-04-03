import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

def dfs(point, n, path, visited):
    print(point + 1, end = ' ')
    for i in range(n):
        if path[point][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i, n, path, visited)
    return


def bfs(point, n, path):
    visited = [0 for _ in range(n)]
    q = deque()
    visited[point] = 1  ## 방문 체크
    q.append(point)

    while q:
        current = q.popleft()
        print(current + 1, end = ' ')
        for i in range(n):
            if path[current][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    path = [[0 for _ in range(N)] for _ in range(N)]
    visited = [0 for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        path[a - 1][b - 1] = 1
        path[b - 1][a - 1] = 1
    visited[V - 1] = 1
    dfs(V-1, N, path, visited)
    print()
    bfs(V - 1, N, path)
