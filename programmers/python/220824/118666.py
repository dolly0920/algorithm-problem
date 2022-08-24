from collections import defaultdict

## https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    answer = ''

    scores = defaultdict(lambda: 0)

    types = [['R','T'], ['C','F'], ['J','M'], ['A','N']]

    for i in range (len(survey)) :
        compare = survey[i]
        choice = choices[i] - 4

        if choice < 0 :
            scores[compare[0]] += abs(choice)
        elif choice > 0 :
            scores[compare[1]] += choice

    for type in types :
        s1 = scores[type[0]]
        s2 = scores[type[1]]

        if s1 > s2 :
            answer += type[0]
        elif s2 > s1 :
            answer += type[1]
        else :
            answer += type[0]

    return answer