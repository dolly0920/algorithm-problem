## https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    if s < n:  ## 만들 수 없는 숫자인 경우
        return [-1]

    x = s // n
    y = s % n

    return [x] * (n - y) + [x + 1] * y
