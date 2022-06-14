import sys

## LCS
class Solution1(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ## LCS (Longest Common Sequence)
        N, M = len(word1), len(word2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]  ## dp[a][b] : to word1[a], word2[b], longest sequence

        for i in range(1, N + 1):  ## word1 index
            for j in range(1, M + 1):  ## word2 index
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = 1 + dp[j - 1][i - 1]
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

        return N + M - (2 * dp[M][N])


## LCS (bottom-up) => 공간 최적화 (이해필요)
class Solution2(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ## LCS
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        ## word2 is longer
        m, n = len(word1), len(word2)
        prev = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            curr = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                if word1[j] == word2[i]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev = curr

        return m + n - (2 * prev[0])