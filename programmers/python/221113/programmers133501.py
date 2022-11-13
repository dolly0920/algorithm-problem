## 구글링 참고..
def solution(distance, scope, times):
    ch = []

    for i in range (len(scope)) : ## 감시병으로 체크
        s, e = sorted(scope[i]) ## 감시 범위
        work, rest = times[i] ## 감시, 휴식 시간
        current = s
        while current <= e : ## 범위에 대헤서 체크
            if 0 < current % (work + rest) <= work : ## 근무중인 거리인 경우
                ch.append(current)
            current += 1

    if ch :
        return min(ch)
    else :
        return distance

if __name__ == "__main__" :
    distance = 10
    scope = [[3, 4], [5, 8]]
    times = [[2, 5], [4, 3]]
    print(solution(distance, scope, times))