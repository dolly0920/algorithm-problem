import sys

sys.stdin = open("../input.txt", "rt")

## 1번째 제출 (시간초과)
def DFS(works, index, time):  ## 남은 일의 배열, 인덱스, 시간
    global answer
    if index == len(works):
        answer = min(answer, getWorkTime(works))
        return

    for i in range(time + 1):
        if works[index] - i < 0:
            continue
        works[index] -= i
        DFS(works, index + 1, time - i)
        works[index] += i
    return


def getWorkTime(works):
    total = 0
    for x in works:
        total += x ** 2
    return total


def solution(n, works):
    global answer
    answer = (50000 ** 2) * 20000  ## 최대값
    DFS(works, 0, n)
    return answer

if __name__ == "__main__" :
    n = int(input())
    works = list(map(int,input().split()))
    print(solution(n, works))