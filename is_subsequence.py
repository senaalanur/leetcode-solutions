class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1  # found a matching character, move to next in s
            j+=1 # always move forward in t

        return i == len(s)