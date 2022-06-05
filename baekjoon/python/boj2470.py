import sys

sys.stdin = open("input.txt", "rt")

def solve(arr, N) :
    answer1 = 0
    answer2 = 0

    left = 0
    right = N-1

    diff = sys.maxsize

    while left < right :
        sum = arr[left] + arr[right]
        if sum == 0 :
            return arr[left], arr[right]
        if abs(sum) < diff :
            diff = abs(sum)
            answer1 = arr[left]
            answer2 = arr[right]
        if sum < 0 :
            left += 1 ## sum값 증가
        else :
            right -= 1 ## sum값 감소
    return answer1, answer2

if __name__ == "__main__" :
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort() ## 오름차순 정렬
    a, b = solve(arr, N)
    print(a, b)