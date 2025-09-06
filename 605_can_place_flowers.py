class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        length = len(flowerbed)

        # Loop through each plot in the flowerbed
        for i in range(length):
            # Check if the current spot is empty
            if flowerbed[i] == 0:
                # Check if the left neighbor is empty or we are at the start
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                # Check if the right neighbor is empty or we are at the end
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)

                # If both neighbors are empty, we can plant a flower here
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Plant a flower
                    n -= 1            # Decrease the number of flowers left to plant

                    # If we have planted all required flowers, return True early
                    if n == 0: 
                        return True
        
        # After the loop, check if we managed to plant enough flowers
        return n <= 0
