## 답 참고 - 누적합
def solution(board, skill):
    answer = 0

    tmp = [[0]*(len(board[0])+1) for _ in range (len(board)+1)]
    for type, r1, c1, r2, c2, degree in skill :
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2+1] -= degree if type == 2 else -degree
        tmp[r2+1][c1] -= degree if type == 2 else -degree
        tmp[r2+1][c2+1] += degree if type == 2 else -degree

    ## 행 기준 누적합
    for i in range (len(tmp)-1) :
        for j in range (len(tmp[0]) - 1) :
            tmp[i][j+1] += tmp[i][j]
    ## 열 기준 누적합
    for i in range (len(tmp[0])-1) :
        for j in range (len(tmp) - 1) :
            tmp[j+1][i] += tmp[j][i]

    ## board 연산
    for i in range (len(board)) :
        for j in range (len(board[0])) :
            if board[i][j] + tmp[i][j] >= 1 :
                answer += 1

    return answer

if __name__ == "__main__" :
    board = [[1,2,3],[4,5,6],[7,8,9]]
    skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
    print(solution(board, skill))