class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Define the set of vowels for quick lookup (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")

        # Convert string to list since Python strings are immutable
        s_list = list(s)

        # Two pointers: one starting from the left, one from the right
        left, right = 0, len(s_list) - 1

        # Process until the pointers meet
        while left < right:

            # Move the left pointer forward until a vowel is found
            while left < right and s_list[left] not in vowels:
                left += 1

            # Move the right pointer backward until a vowel is found
            while left < right and s_list[right] not in vowels:
                right -= 1

            # Swap the vowels
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        # Join the list back into a string and return
        return "".join(s_list)
