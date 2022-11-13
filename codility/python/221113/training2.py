# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    checked = set()

    for number in A:
        if number in checked:
            checked.remove(number)
        else:
            checked.add(number)

    for answer in checked:
        return answer

if __name__ == "__main__" :
    print(solution([9,3,9,3,9,7,9]))