# equal_row_and_column_pairs.py
# Problem: Equal Row and Column Pairs
# Approach: Convert each row and each column into tuples, count their occurrences, 
# then sum the products of matching row and column counts to get total equal pairs.

from collections import Counter

def equalPairs(grid):
    """
    Returns the number of pairs (ri, cj) such that row ri and column cj are equal.
    """
    # Convert each row to a tuple and count occurrences
    rows = Counter(tuple(row) for row in grid)
    # Convert each column to a tuple (using zip(*grid)) and count occurrences
    cols = Counter(tuple(col) for col in zip(*grid))
    # Multiply counts for each matching tuple and sum to get total equal pairs
    return sum(rows[t] * cols[t] for t in rows)

# Example test cases
if __name__ == "__main__":
    grid1 = [[3,2,1],[1,7,6],[2,7,7]]
    print(equalPairs(grid1))  # Output: 1

    grid2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(equalPairs(grid2))  # Output: 3
