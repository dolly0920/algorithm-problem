class Solution1(object): ## memorization
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        memo = [[-1] * length for _ in range(length)]

        def dfs(x, y):
            if y == length:
                return 0

            if memo[y][x] != -1:
                return memo[y][x]

            left_sum = triangle[y][x] + dfs(x, y + 1)
            right_sum = triangle[y][x] + dfs(x + 1, y + 1)

            memo[y][x] = min(left_sum, right_sum)
            return memo[y][x]

        return dfs(0, 0)


class Solution2(object): ## bottom-up dp
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ## Bottom-up dp
        n = len(triangle)
        dp = [[-1] * n for _ in range(n)]  ## dp[x][y] : meaning -> in (x,y) min value
        dp[n - 1] = triangle[n - 1]

        for row in range(n - 2, -1, -1):
            for col in range(row + 1):
                from_bottom = triangle[row][col] + dp[row + 1][col]
                from_right_bottom = triangle[row][col] + dp[row + 1][col + 1]
                dp[row][col] = min(from_bottom, from_right_bottom)

        return dp[0][0]


class Solution3(object): ## bottomup-dp, space optimization
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ## Bottom-up dp, Space optimized
        n = len(triangle)
        next_row = triangle[-1][:]
        curr_row = [0] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                lower_left = triangle[i][j] + next_row[j]
                lower_right = triangle[i][j] + next_row[j + 1]
                curr_row[j] = min(lower_left, lower_right)

            curr_row, next_row = next_row, curr_row

        return next_row[0]