class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        candy = [1] * length

        for i in range(1, length):
            if ratings[i] > ratings[i - 1] and candy[i] <= candy[i - 1]:
                candy[i] = candy[i - 1] + 1

        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
                candy[i] = candy[i + 1] + 1

        return sum(candy)