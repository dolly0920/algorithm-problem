import sys

sys.stdin = open("../input.txt", "rt")

## 1 : 정확성 통과, 효율성 실패
def operate(k):
    global stones_t

    index = 0  ## 시작
    while True:
        flag = True
        for i in range(1, k + 1):
            if index + i < len(stones_t) and stones_t[index + i] > 0:
                stones_t[index + i] -= 1
                index = index + i
                flag = False
                break
            elif index + i >= len(stones_t):
                return True
        if flag:
            return False


def solution(stones, k):
    global stones_t
    answer = 0

    stones_t = [0] + stones

    while True:
        result = operate(k)
        if result:
            answer += 1
        else:
            break

    return answer

if __name__ == "__main__" :
    stones = list(map(int, input().split()))
    k = int(input())
    print(solution(stones, k))