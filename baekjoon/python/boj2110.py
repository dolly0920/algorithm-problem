import sys

sys.stdin = open("input.txt", "rt")

if __name__ == "__main__" :
    N, C = map(int, input().split())
    house = []
    answer = 0
    for _ in range (N) :
        s = int(input())
        house.append(s)

    ## 이분 탐색
    house.sort()

    start = 1 ## 최소 거리
    end = house[-1] - house[0] ## 최대 거리

    while start <= end :
        mid = (start + end) // 2 ## 간격의 최솟값

        count = 1
        current = house[0] ## 첫 집의 좌표
        for i in range (1, N) :
            if house[i] >= current + mid : ## 최솟값(거리)보다 크거나 같은 경우
                current = house[i] ## 현재 위치 갱신
                count += 1 ## 설치한 집의 갯수 + 1

        if (count >= C) : ## 설치한 와이파이 갯수가 C보다 많은 경우 간격을 더 넓게하는 것이 가능하다
            start = mid+1
            answer = mid ## 가능한 값이므로 answer로 저장
        else : ## 불가능한 경우 간격을 줄인다.
            end = mid-1

    print(answer)
