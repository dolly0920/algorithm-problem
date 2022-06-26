## Time Limit Exceed
class Solution1(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        ## two pointer, memorization(dp)
        length = len(cardPoints)
        dp = [[-1] * length for _ in range(length)]  ## dp[left][right] : when left - right range : max sum

        def solve(left, right, s, depth):
            if depth == k:
                return s

            if dp[left][right] != -1:
                return dp[left][right]

            left_sum = solve(left + 1, right, s + cardPoints[left], depth + 1)
            right_sum = solve(left, right - 1, s + cardPoints[right], depth + 1)
            dp[left][right] = max(left_sum, right_sum)

            return dp[left][right]

        return solve(0, length - 1, 0, 0)

## Passed
class Solution2(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        length = len(cardPoints)
        remain_arr_length = length - k

        remain_sum = sum(cardPoints[:remain_arr_length])

        min_sum = remain_sum

        for i in range(remain_arr_length, length):
            remain_sum += cardPoints[i]
            remain_sum -= cardPoints[i - remain_arr_length]
            min_sum = min(min_sum, remain_sum)

        return sum(cardPoints) - min_sum