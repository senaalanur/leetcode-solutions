# find_difference_of_two_arrays.py
# Problem: Find Difference of Two Arrays
# Approach: Use sets — subtract one set from the other in both directions to find unique elements.
# This removes duplicates and finds elements in nums1 not in nums2 and vice versa.

def findDifference(nums1, nums2):
    """
    Returns a list of two lists:
    - answer[0]: elements in nums1 not in nums2
    - answer[1]: elements in nums2 not in nums1
    """
    set1, set2 = set(nums1), set(nums2)
    return [list(set1 - set2), list(set2 - set1)]

# Example test cases
if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    print(findDifference(nums1, nums2))  # Output: [[1, 3], [4, 6]]

    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    print(findDifference(nums1, nums2))  # Output: [[3], []]
