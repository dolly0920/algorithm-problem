import sys

sys.stdin = open("../input.txt", "rt")

def solution(stones, k) :
    answer = 0

    left = 0
    right = max(stones)

    while left <= right :
        mid = (left + right) // 2

        if isPossible(stones, k, mid) :
            left = mid + 1
            answer = max(answer, mid)
        else :
            right = mid - 1
    return answer

def isPossible(stones, k, friends) :
    skip = 0

    for stone in stones :
        if stone - friends < 0 : ## 해당 디딤돌은 건너 뛰어야함
            skip += 1
        else :
            skip = 0

        if skip == k : ## 연속으로 밟을 수 없는 디딤돌이 k개인 경우 (이 경우에 건너뛰게 되는 디딤돌의 갯수는 k+1)
            return False
    return True

if __name__ == "__main__" :
    stones = list(map(int, input().split()))
    k = int(input())
    print(solution(stones, k))