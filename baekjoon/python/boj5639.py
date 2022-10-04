import sys

sys.setrecursionlimit(10**6)

sys.stdin = open("input.txt", "rt")

## 다시 풀어볼 것 - 제대로 이해안되는 상태
def DFS(start, end) :
    if start > end :
        return

    mid = end + 1 ## 범위 안에 루트보다 큰 값이 없을 때
    for i in range (start+1, end+1) : ## numbers[start] - 루트 노드
        if numbers[start] < numbers[i] :
            mid = i
            break

    DFS(start+1, mid-1)
    DFS(mid, end)
    print(numbers[start])


if __name__ == "__main__" :
    numbers = []
    while True :
        try :
            numbers.append(int(input()))
        except :
            break
    DFS(0, len(numbers)-1)
