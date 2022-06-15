from collections import deque

## 답 참고함 나중에 다시 풀어볼 것
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ## LCS

        words.sort(key=len)

        dp = {}  ## dp dictionary -> dp[x] : x(word)'s longest sequence number
        res = 1
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]  ## exception word[i]
                if prev in dp:
                    dp[word] = dp[prev] + 1
                    res = max(res, dp[word])

        return res