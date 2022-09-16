import heapq

## https://school.programmers.co.kr/learn/courses/30/lessons/42628
## 시간초과 테스트케이스가 없기 때문에 좀 더 좋은 풀이법에 대해 생각 필요!
def solution(operations):
    min_heap = []
    exist_count = 0

    for operation in operations:
        command, num = operation.split(' ')
        if command == 'I':
            exist_count += 1
            heapq.heappush(min_heap, int(num))
        elif command == 'D' and exist_count > 0:
            exist_count -= 1
            if num == '1':  ## 최댓값 제거
                min_heap = heapq.nlargest(len(min_heap), min_heap)[1:]
                heapq.heapify(min_heap)
            else:
                heapq.heappop(min_heap)

    if exist_count == 0:
        return [0, 0]

    return [heapq.nlargest(len(min_heap), min_heap)[0], heapq.heappop(min_heap)]