class Solution1(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## when increasing, max
        result = [nums[0]]

        i = 1
        while i < len(nums) and nums[i] - nums[i - 1] == 0:
            i += 1
        if i < len(nums):
            result.append(nums[i])

        while i < len(nums):
            if result[-1] - result[-2] > 0:  ## increasing
                while i < len(nums) and nums[i] >= nums[i - 1]:
                    result[-1] = nums[i]
                    i += 1
                if i < len(nums):
                    result.append(nums[i])
                    i += 1
            else:  ## descresing
                while i < len(nums) and nums[i] <= nums[i - 1]:
                    result[-1] = nums[i]
                    i += 1
                if i < len(nums):
                    result.append(nums[i])
                    i += 1
        return len(result)

class Solution2(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        increase = 1 ## to current index, max (last) increase sequence length
        decrease = 1 ## to current index, max (last) decrease sequence length
        for i in range (1, len(nums)) :
            if nums[i] > nums[i-1] : ## increase
                increase = decrease + 1
            elif nums[i] < nums[i-1] : ## decrease
                decrease = increase + 1
        answer = min(len(nums), max(increase, decrease))
        return answer