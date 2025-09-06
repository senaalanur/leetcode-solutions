class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        # Find the current maximum number of candies any kid has
        maxCandies = max(candies)

        # For each kid, check if adding extraCandies makes them reach or exceed maxCandies
        # Return a list of booleans indicating the result for each kid
        return [(curNum + extraCandies >= maxCandies) for curNum in candies]
