def solution(targets):
    answer = 0

    targets.sort(key = lambda x: [x[1],x[0]])

    cur_s = cur_e = 0

    for s,e in targets :
        if s >= cur_e :
            answer += 1
            cur_e = e

    return answer

if __name__ == "__main__" :
    targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
    print(solution(targets))