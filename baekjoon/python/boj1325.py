import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

def bfs(start) :
    count = 0
    visited = [False for _ in range (N+1)]
    q = deque()
    q.append(start)
    visited[start] = True

    while q :
        current = q.popleft()
        count += 1
        for c in trusted[current]:
            if not visited[c]:
                visited[c] = True
                q.append(c)
    return count

if __name__ == "__main__" :
    N, M = map(int, input().split())
    trusted = [[] for _ in range (N+1)]
    for _ in range (M) :
        a, b = map(int, input().split())
        trusted[b].append(a)

    max = -1
    answer = []
    for s in range (1, N+1) :
        polluted = bfs(s)
        if polluted > max :
            max = polluted
            answer = [s]
        elif polluted == max :
            answer.append(s)
    print(*answer)
