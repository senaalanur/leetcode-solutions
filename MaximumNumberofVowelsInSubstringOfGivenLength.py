class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')

        # Initial window count
        count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = count

        # Two pointers: slide window
        for i in range(k, len(s)):

            # Add new char (right side)
            if s[i] in vowels:
                count += 1

            # Remove left char (left side)
            if s[i - k] in vowels:
                count -= 1

            # Update max
            max_count = max(max_count, count)

        return max_count
        