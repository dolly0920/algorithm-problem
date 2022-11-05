## 시간초과 발생 : why? (list sum 함수의 시간 복잡도도 O(n)인데 통과됨)
def solution(elements):
    number = set()

    for i in range (1, len(elements) + 1):  ## 수열의 길이
        for start in range (len(elements)) : ## 시작점
            index = start
            tmp = 0
            for _ in range (i) :
                tmp += elements[index%len(elements)]
                index += 1
            number.add(tmp)

    return len(number)

if __name__ == "__main__" :
    elements = [7,9,1,1,4]
    print(solution(elements))