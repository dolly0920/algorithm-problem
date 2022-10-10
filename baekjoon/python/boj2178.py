import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def BFS(r, c) : ## (r,c) -> (N-1, M-1)
    q = deque()

    visited[r][c] = 1
    q.append((r,c))

    answer = 1
    while q :
        q_len = len(q)
        answer += 1
        while q_len > 0 :
            q_len -= 1
            r, c = q.popleft()
            for i in range (4) :
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= M :
                    continue
                if visited[nr][nc] == 1 or arr[nr][nc] == 0 :
                    continue
                if nr == N-1 and nc == M-1 :
                    return answer
                visited[nr][nc] = 1
                q.append((nr,nc))
    return -1


if __name__ == "__main__" :
    N, M = map(int, input().split())
    arr = []
    for _ in range (N) :
        arr.append(list(map(int, input())))

    visited = [[0]*M for _ in range (N)]
    print(BFS(0, 0))