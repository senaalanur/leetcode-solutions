class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            # Expand the window
            if nums[right] == 0:
                zeros += 1

            # Shrink window if zeros > k
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
