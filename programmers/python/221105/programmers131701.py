def solution(elements):
    transformed = elements + elements
    number = set()

    for i in range(1, len(elements) + 1):  ## 수열의 길이
        for start in range(len(elements)):
            number.add(sum(transformed[start:start + i]))

    return len(number)

if __name__ == "__main__" :
    elements = [7,9,1,1,4]
    print(solution(elements))