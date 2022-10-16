import sys
from collections import defaultdict

sys.stdin = open("../input.txt", "rt")

def solution(gems):
    answer = [0, len(gems)] ## 처음에는 배열 전체 범위

    size = len(set(gems))

    gems_dict = defaultdict(lambda : 0) ## default value 0

    left, right = 0, 0
    gems_dict[gems[left]] += 1

    length = len(gems)

    while left < length and right < length :
        if len(gems_dict) == size : ## 모든 보석들이 담겨 있는 경우
            if right - left < answer[1] - answer[0] : ## answer 갱신
                answer = [left, right]
            gems_dict[gems[left]] -= 1
            if gems_dict[gems[left]] == 0:
                del gems_dict[gems[left]]
            left += 1
        else : ## 보석이 부족한 경우 범위를 넓힌다
            right += 1

            if right == length : ## 인덱스 초과
                break

            gems_dict[gems[right]] += 1 ## 보석 추가

    return [answer[0]+1, answer[1]+1]

if __name__ == "__main__" :
    gems = list(input().split())
    print(solution(gems))