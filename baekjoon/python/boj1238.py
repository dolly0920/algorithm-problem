import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")

def dijkstra(start) :
    d = [INF] * (N)

    pq = []
    d[start] = 0  ## start
    hq.heappush(pq, (0, start))

    while pq :
        cur_f, cur_l = hq.heappop(pq)
        for destination, c in cost[cur_l].items() : ## 목적지, 비용
            if cur_f + c < d[destination] :
                d[destination] = cur_f + c
                hq.heappush(pq, (d[destination], destination))
    return d

if __name__ == "__main__" :
    N, M, X = map(int, input().split())

    INF = sys.maxsize
    cost = [{} for _ in range (N)]

    for _ in range (M) :
        start, end, c = map(int, input().split())
        cost[start-1][end-1] = c

    back = dijkstra(X-1)
    answer = -1
    for start in range (N) :
        go = dijkstra(start)
        answer = max(answer, go[X-1] + back[start])

    print(answer)
