class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n   # output array; start with 1’s as neutral element of multiplication

        # ----- Prefix products -----
        # answer[i] will hold the product of all numbers to the LEFT of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # -----  Suffix products -----
        # Multiply by product of all numbers to the RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
