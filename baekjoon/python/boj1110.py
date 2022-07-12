import sys

sys.stdin = open("input.txt", "rt")

def rnumber(number) :
    return number % 10

def operate(number) :
    length = len(str(number))
    answer = 0
    for i in range (length) :
        answer += int(str(number)[i])
    return answer

if __name__ == "__main__" :
    N = int(input())
    count = 0
    target = N

    while True :
        next = N
        if next < 10 :
            next *= 10
        first = rnumber(N)
        second = rnumber(operate(next))
        next = 10*first + second
        count += 1
        if next == target:
            break
        N = next
    print(count)

