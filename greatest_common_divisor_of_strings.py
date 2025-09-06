class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # Get lengths of both strings
        len1, len2 = len(str1), len(str2)

        # Helper function to check if a substring of length l is a divisor of both strings
        def isDivisor(l):
            # Both lengths must be divisible by l
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l
            # Check if repeating the substring reconstructs both strings
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # Try possible substring lengths from largest to smallest
        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]  # Found greatest common divisor string

        return ""  # No common divisor string found


        