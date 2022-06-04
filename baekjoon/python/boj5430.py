import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

def solve(commands, n, arr_str) :

    ## arr_str -> arr
    arr = deque()
    if n != 0 :
        arr = deque(list(arr_str[1:-1].split(',')))

    rev_count = 0

    for command in commands :
        if command == 'R' :
            rev_count += 1
        elif command == 'D' :
            if len(arr) == 0 :
                return "error"
            if rev_count % 2 == 0 :
                arr.popleft()
            else :
                arr.pop()
    if rev_count % 2 == 1 :
        arr.reverse()
    ## string 변환 (여백 없는 string list형태로 변환 필요)
    return "[" + ",".join(list(arr)) + "]"



if __name__ == "__main__" :
    ## R : 순서 뒤집는 함수, D : 첫 번째 함수를 버리는 함수
    T = int(input())
    for _ in range (T) :
        commands = input()
        n = int(input())
        arr_str = input()
        print(solve(commands, n, arr_str))
