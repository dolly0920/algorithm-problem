import sys

sys.stdin = open("./input.txt", "rt")

## 1번째 풀이 - 오답 (testcase1 실패)
def solution(gems):
    answer = []

    length = len(gems)

    gems_list = set(gems)  ## 중복제거
    distinct_count = len(gems_list)

    bucket = set()

    start = 0
    end = 0

    tmp = 100000

    while start <= end and start < length and end < length:
        bucket.add(gems[start])
        bucket.add(gems[end])

        if len(bucket) == distinct_count and end - start < tmp:
            tmp = end - start
            answer = [start + 1, end + 1]

        if start + 1 < length and gems[start] == gems[start + 1]:
            start += 1
        elif len(bucket) < distinct_count:
            end += 1
        else:
            bucket.remove(gems[start]) ## 여기서 이렇게 삭제하게 되면 범위 안에 있는 문자도 중복되어 지워질 가능성이 있다.
            start += 1

    return answer

if __name__ == "__main__" :
    gems = list(input().split())
    print(solution(gems))
