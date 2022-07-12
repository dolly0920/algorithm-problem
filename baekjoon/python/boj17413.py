import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

def extract(q) :
    answer = ""
    while q :
        answer += q.popleft()
    return answer

def extract_reverse(q) :
    answer = ""
    while q :
        answer += q.pop()
    return answer

if __name__ == "__main__" :
    inputString = input()
    message = deque()

    tag_flag = False ## true : tag, false : tag x
    answer = ""
    for str in inputString :
        if str == '<' :
            answer += extract_reverse(message)
            tag_flag = True
            message.append(str)
        elif str == '>' :
            tag_flag = False
            message.append(str)
            answer += extract(message)
        elif tag_flag :
            message.append(str)
        else :
            if str == " " :
                answer += extract_reverse(message)
                answer += " "
            else :
                message.append(str)
    if message :
        answer += extract_reverse(message)
    print(answer)

## solution2
# a=input()
# b=a.replace('>','<').split('<')
# s=""
# for i in range(len(b)):
#   if i%2:
#       s+='<'+b[i]+'>'
#   else:
#     c=b[i].split()
#     s+=' '.join([d[::-1] for d in c])
# print(s)