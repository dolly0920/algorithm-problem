import sys
sys.setrecursionlimit(10000)

sys.stdin = open("./input.txt", "rt")

## 2번째 시도 (시간 초과는 발생, 재귀깊이 추가)
def DFS(works, index, time, cost) :
    global answer
    if index == len(works) :
        answer = min(answer, cost)
        return

    if cost >= answer :
        return

    for i in range (time+1) :
        if works[index] - i < 0 :
            continue
        works[index] -= i
        DFS(works, index+1, time-i, cost+(works[index]**2))
        works[index] += i

def solution(n, works):
    global answer
    if n >= sum(works) :
        return 0
    answer = (50000**2)*20000
    DFS(works, 0, n, 0)
    return answer

if __name__ == "__main__" :
    n = int(input())
    works = list(map(int, input().split()))
    print(solution(n, works))