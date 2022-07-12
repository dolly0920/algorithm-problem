import sys

sys.stdin = open("input.txt", "rt")

def operate(n) :
    answer = n
    for num in str(n) :
        answer += int(num)
    return answer

if __name__ == "__main__" :
    check = [True] * 10001
    for i in range (1, 10001) :
        result = operate(i)
        if result < 10001 :
            check[result] = False
    for i in range (1, 10001) :
        if check[i] :
            print(i)

