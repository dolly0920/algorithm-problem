## link : https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    global answer
    answer = 0
    length = len(numbers)

    def DFS(cur_index, result) :
        global answer
        if cur_index == length :
            if result == target :
                answer += 1
            return
        DFS(cur_index + 1, result + numbers[cur_index])
        DFS(cur_index + 1, result - numbers[cur_index])

    DFS(0,0)

    return answer


if __name__ == "__main__" :
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))