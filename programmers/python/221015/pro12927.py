import sys
import heapq as hq

sys.stdin = open("./input.txt", "rt")

## https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%BC%EA%B7%BC-%EC%A7%80%EC%88%98-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C-level3-%ED%8C%8C%EC%9D%B4%EC%8D%AC-heap
## 답안 (최대힙 활용)
def solution(n, works):
    if n >= sum(works) :
        return 0

    works = [-w for w in works]
    hq.heapify(works) ## 최대힙

    for _ in range (n) : ## 각각의 요소에서 1씩 빼면서 제곱합을 최소로 만든다.
        x = hq.heappop(works) ## 최댓값 빼기 (-로 반대로 되어있음)
        hq.heappush(works, x+1)
    return sum([w**2 for w in works])

if __name__ == "__main__" :
    n = int(input())
    works = list(map(int, input().split()))
    print(solution(n, works))