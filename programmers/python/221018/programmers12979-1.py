import sys
import math

sys.stdin = open("../input.txt", "rt")

def solution(n, stations, w):
    answer = 0
    length = w * 2 + 1

    s = 1
    for station in stations:
        left = station - w - 1
        right = station + w + 1

        answer += math.ceil((left - s + 1) / length)
        s = right

    if s <= n:
        answer += math.ceil((n - s + 1) / length)

    return answer

if __name__ == "__main__" :
    N = int(input()) ##
    station = list(map(int, input().split()))
    W = int(input())
    print(solution(N, station, W))