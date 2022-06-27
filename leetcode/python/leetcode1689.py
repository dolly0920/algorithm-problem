class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """

        answer = -1

        for i in range(len(n)):
            answer = max(answer, int(n[i]))

        return answer