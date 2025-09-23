class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter

        count = Counter()   # to store frequency of numbers seen
        operations = 0      # number of valid pairs

        for num in nums:
            target = k - num

            # if target exists, we can form a pair
            if count[target] > 0:
                operations += 1
                count[target] -= 1  # remove one occurrence of target
            else:
                # store num for future pairing
                count[num] += 1

        return operations
