# 004_close_strings.py
# Problem: Determine if Two Strings Are Close
# Approach: Two strings are "close" if they have the same set of characters and the same frequency counts (in any order).

from collections import Counter

def closeStrings(word1, word2):
    """
    Returns True if word1 and word2 are close according to the rules:
    - You can swap any two characters any number of times.
    - You can transform all occurrences of one character to another and vice versa.
    """
    # Check if both words have the same characters
    if set(word1) != set(word2):
        return False
    # Check if frequency counts of characters are the same (order doesn't matter)
    return sorted(Counter(word1).values()) == sorted(Counter(word2).values())

# Example test cases
if __name__ == "__main__":
    print(closeStrings("abc", "bca"))      # Output: True
    print(closeStrings("a", "aa"))         # Output: False
    print(closeStrings("cabbba", "abbccc"))# Output: True
