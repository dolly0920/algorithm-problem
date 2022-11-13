from collections import deque

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.8.10
    if len(A) == 0 or len(A) == 1:
        return A
    A = deque(A)
    for _ in range (K%len(A)) :
        A.rotate(1)
    return list(A)


if __name__ == "__main__" :
    print(solution([], 1))