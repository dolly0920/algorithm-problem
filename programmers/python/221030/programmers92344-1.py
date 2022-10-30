def operate(board, r1, c1, r2, c2, degree) : ## 공격, 회복
    n = len(board)  ## 행 길이
    for i in range (r1, r2+1) :
        for j in range (c1, c2+1) :
            board[i][j] += degree
    return board

## 정확도 pass, 효율성 fail
def solution(board, skill):
    answer = 0

    n = len(board) ## 행 길이
    state = board ## 초기값

    for type, r1, c1, r2, c2, degree in skill :
        if type == 1 :
            state = operate(state, r1, c1, r2, c2, -degree)
        else :
            state = operate(state, r1, c1, r2, c2, degree)

    for i in range (n) :
        for j in range (len(state[0])) :
            if state[i][j] >= 1 :
                answer += 1
    return answer

if __name__ == "__main__" :
    board = [[1,2,3],[4,5,6],[7,8,9]]
    skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
    print(solution(board, skill))