import sys
from collections import deque

sys.stdin = open("input.txt")

if __name__ == "__main__" :
    N = int(input())

    ## 소수 구하기 (에라토스테네스의 체)
    sieve = [True] * (N+1)
    m = int(N ** 0.5)

    for i in range (2, m+1) :
        if sieve[i] :
            for j in range (i+i, N+1, i) :
                sieve[j] = False

    ## 합 구하기
    answer = 0
    numbers = deque()
    sum_value = 0
    for i in range (2, N+1) :
        if sieve[i] == False : ## 소수가 아닌 경우
            continue
        sum_value += i
        numbers.append(i)
        if sum_value == N:
            answer += 1
        elif sum_value > N:
            while numbers and sum_value > N :
                num = numbers.popleft()
                sum_value -= num
            if sum_value == N :
                answer += 1
    print(answer)



