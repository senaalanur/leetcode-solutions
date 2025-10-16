# remove_stars_from_string.py
# Problem: Removing Stars From a String
# Difficulty: Easy
# Topics: String, Stack
# 
# Description:
# Given a string s containing lowercase letters and stars '*', each star removes the closest 
# non-star character to its left along with the star itself. Return the resulting string.
# 
# Example:
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation:
# - The first '*' removes 't' → "lee*cod*e"
# - The next '*' removes 'e' → "lecod*e"
# - The next '*' removes 'd' → "lecoe"

def removeStars(s: str) -> str:
    # Use a stack (list) to store characters as we go
    stack = []

    # Loop through each character in the string
    for ch in s:
        if ch == '*':
            # If current character is '*', remove the last added letter (undo operation)
            stack.pop()
        else:
            # Otherwise, add the character to our stack
            stack.append(ch)

    # Join the characters in the stack to form the final string
    return ''.join(stack)


# Example usage (you can comment this out before committing if you prefer clean output)
if __name__ == "__main__":
    print(removeStars("leet**cod*e"))  # Output: lecoe
    print(removeStars("erase*****"))   # Output: ""
