import sys

sys.stdin = open("input.txt", "rt")

def caculate(number) :
    answer = 0
    length = len(str(number))

    for i in range (1, length) :
        answer += 9*(10**(i-1))*i

    first_num = 10**(length-1)

    answer += length*(number-first_num+1)

    return answer

if __name__ == "__main__" :
    N = int(input())
    ## 1 ~ 9 : 9, 10 ~ 99 : 90, 100 ~ 999 : 900, 1000 ~ 9999 : 9000
    print(caculate(N))


