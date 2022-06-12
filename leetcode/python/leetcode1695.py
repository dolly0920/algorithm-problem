from collections import deque

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = -1
        q = deque()
        check_num = set()

        sum = 0
        for number in nums:
            if len(q) > 0 and number in check_num:
                while q:
                    first = q.popleft()
                    sum -= first
                    check_num.remove(first)
                    if first == number:
                        break
            sum += number
            q.append(number)
            check_num.add(number)
            answer = max(answer, sum)
        return answer