from collections import deque

## timelimit exceed
class Solution1(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        dp = [-10001] * length  ## dp[n] : n부터 배열 끝까지의 최댓값
        dp[length - 1] = nums[length - 1]
        q = deque()
        q.append((length - 1, dp[length - 1]))  ## cur_index, cur_sum

        while q:
            cur_index, cur_sum = q.popleft()

            for i in range(1, k + 1):
                if cur_index - i >= 0 and cur_sum + nums[cur_index - i] > dp[cur_index - i]:
                    dp[cur_index - i] = cur_sum + nums[cur_index - i]
                    q.append((cur_index - i, dp[cur_index - i]))
        return dp[0]

## Passed : (답 참고)
class Solution2(object):
    ## 다시 한번 풀어볼 것.
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        q = deque([0])  ## index queue

        for i in range(1, n):
            nums[i] += nums[q[0]]
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
        return nums[-1]