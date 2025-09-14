class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')   # smallest value seen so far
        second = float('inf')  # second smallest value seen so far

        for n in nums:
            if n <= first:
                first = n            # found new smallest
            elif n <= second:
                second = n           # found candidate for second
            else:
                # n is greater than both first and second
                # so we have first < second < n
                return True
        return False
