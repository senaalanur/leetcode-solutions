class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, automatically removing extra spaces
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join them back together with a single space
        return " ".join(reversed_words)
