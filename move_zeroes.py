class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0  # position to place the next non-zero element

        # fast pointer scans through the array
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        # fill the remaining positions with 0
        for i in range(slow, len(nums)):
            nums[i] = 0
