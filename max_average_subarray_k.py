class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        
        # 1) compute sum of first window (first k elements)
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # 2) slide the window to the right one element at a time
        for i in range(k, n):
            # add new right element, remove old left element (O(1) update)
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        # 3) average = sum / k
        return float(max_sum) / k

        