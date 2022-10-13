import sys

sys.stdin = open("input.txt", "rt")

def caculate(length) :
    cnt, tmp = 1, 0
    for i in range (len(arr)) :
        if tmp + arr[i] <= length :
            tmp += arr[i]
        else :
            cnt += 1
            tmp = arr[i]
    return cnt

if __name__ == "__main__" :
    N, M = map(int, input().split()) ## 강의의 수, 블루레이의 수
    arr = list(map(int, input().split())) ## 강의 길이 리스트

    start = 1
    end = 10000 * 100000

    answer = sum(arr)
    max_length = max(arr)

    while start <= end :
        mid = (start + end) // 2

        if mid < max_length : ## 불필요한 연산 막기
            start = mid + 1
            continue

        cnt = caculate(mid)

        if cnt <= M :
            answer = min(answer, mid)
            end = mid-1
        else :
            start = mid+1

    print(answer)