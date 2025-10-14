# unique_number_of_occurrences.py
# Problem: Unique Number of Occurrences
# Approach: Count each number's frequency, then check if all frequency counts are unique using a set.

from collections import Counter

def uniqueOccurrences(arr):
    """
    Returns True if the number of occurrences of each value in the array is unique, False otherwise.
    """
    count = Counter(arr)  # Count frequency of each number
    return len(count.values()) == len(set(count.values()))  # Check if all frequencies are unique

# Example test cases
if __name__ == "__main__":
    arr1 = [1, 2, 2, 1, 1, 3]
    print(uniqueOccurrences(arr1))  # Output: True

    arr2 = [1, 2]
    print(uniqueOccurrences(arr2))  # Output: False

    arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(uniqueOccurrences(arr3))  # Output: True
