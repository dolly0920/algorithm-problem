import sys

sys.stdin = open("input.txt", "rt")

def cal(r, c) :
    return (r//3)*3 + (c//3)

def DFS(index) :

    if index == 81 :
        for b in board :
            print("".join(map(str, b)))
        return True

    r = index // 9
    c = index % 9

    if board[r][c] : ## 숫자가 들어가있는 경우 다음 인덱스 탐색
        return DFS(index + 1)
    else :
        for num in range (1, 10) : ## num는 들어가게될 숫자
            if not row[r][num] and not col[c][num] and not area[cal(r, c)][num] :
                row[r][num], col[c][num], area[cal(r, c)][num] = True, True, True
                board[r][c] = num
                if DFS(index + 1) :
                    return True
                board[r][c] = 0
                row[r][num], col[c][num], area[cal(r, c)][num] = False, False, False
    return False
if __name__ == "__main__" :
    board = []
    for _ in range (9) :
        board.append(list(map(int, input())))

    ## 가로, 세로, 구역별 가능한 숫자 파악
    row = [[False]*10 for _ in range (9)] ## row[i][j] : i번째 row의 j라는 숫자 존재 여부
    col = [[False]*10 for _ in range (9)]
    area = [[False]*10 for _ in range (9)]

    for i in range (9) :
        for j in range (9) :
            if board[i][j] :
                row[i][board[i][j]] = True
                col[j][board[i][j]] = True
                area[cal(i, j)][board[i][j]] = True
    DFS(0)
