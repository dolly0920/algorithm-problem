import sys

sys.stdin = open("../input.txt", "rt")

## 정답 참고했음 - 이해 필요
def solution(stones, k):
    answer = 0

    left, right = 1, max(stones)

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for stone in stones:
            if stone - mid <= 0:  ## mid명이 stone을 밟았을 때
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left

if __name__ == "__main__" :
    stones = list(map(int, input().split()))
    k = int(input())
    print(solution(stones, k))