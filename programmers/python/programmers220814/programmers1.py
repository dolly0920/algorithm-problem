// https://school.programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    arr = [[row*columns + col + 1 for col in range (columns)] for row in range (rows)]
    answer = []

    for x1, y1, x2, y2 in queries :
        target, arr = rotate(x1-1, y1-1, x2-1, y2-1, arr)
        answer.append(target)

    return answer

def rotate(x1, y1, x2, y2, arr) :
    target = arr[x1][y1] ## 시작
    tmp = arr[x1][y1]

    ## 왼쪽
    for x in range (x1, x2) :
        arr[x][y1] = arr[x+1][y1]
        target = min(target, arr[x+1][y1])

    ## 아래쪽
    for y in range (y1, y2) :
        arr[x2][y] = arr[x2][y+1]
        target = min(target, arr[x2][y+1])

    ## 오른쪽
    for x in range (x2, x1, -1) :
        arr[x][y2] = arr[x-1][y2]
        target = min(target, arr[x-1][y2])

    ## 위쪽
    for y in range (y2, y1, -1) :
        if (y-1 == y1) :
            arr[x1][y] = tmp
            target = min(target, tmp)
        else :
            arr[x1][y] = arr[x1][y-1]
            target = min(target, arr[x1][y-1])
    return target, arr