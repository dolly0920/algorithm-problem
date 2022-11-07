from collections import deque

## https://school.programmers.co.kr/learn/courses/30/lessons/118667
## 통과는 했지만 효율성이 좋지 못함
def solution(queue1, queue2):
    answer = 0

    sum_a = sum(queue1)
    sum_b = sum(queue2)

    if (sum_a + sum_b) % 2 != 0:
        return -1
    target = (sum_a + sum_b) // 2

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    visited = set()

    while True:
        if (sum_a, sum_b, queue1[0], queue2[0]) in visited:
            return -1
        visited.add((sum_a, sum_b, queue1[0], queue2[0]))
        if sum_a > sum_b:
            tmp = queue1.popleft()
            if tmp > target:
                return -1
            sum_a -= tmp
            queue2.append(tmp)
            sum_b += tmp
        elif sum_a < sum_b:
            tmp = queue2.popleft()
            if tmp > target:
                return -1
            sum_b -= tmp
            queue1.append(tmp)
            sum_a += tmp
        else:
            break
        answer += 1

    return answer

if __name__ == "__main__" :
    queue1 = [3, 2, 7, 2]
    queue2 = [4, 6, 5, 1]
    print(solution(queue1, queue2))