"""
Optimized and efficient code patterns.
This file demonstrates best practices and performance improvements.
"""

import time
from collections import Counter


def efficient_string_concatenation(items):
    """
    FAST: Using join() method with a list comprehension.
    Only creates one final string object.
    """
    return ",".join(str(item) for item in items)


def efficient_list_append(n):
    """
    FAST: Using list comprehension or proper append.
    Much more efficient than creating new lists.
    """
    return [i * i for i in range(n)]


def efficient_computation_in_loop(data, search_term):
    """
    FAST: Computing invariants outside the loop.
    The upper() call on search_term happens only once.
    """
    search_upper = search_term.upper()
    return [item for item in data if item.upper() == search_upper]


def efficient_nested_loop_search(list1, list2):
    """
    FAST: Using set intersection - O(n+m) complexity.
    Converts one list to a set for O(1) lookup.
    """
    return list(set(list1) & set(list2))


def efficient_filtering(numbers):
    """
    FAST: Single pass with combined conditions.
    Uses a single list comprehension.
    """
    return [num for num in numbers if num > 0 and num % 2 == 0 and num < 100]


def efficient_dictionary_lookup(data_list):
    """
    FAST: Using Counter for O(n) complexity.
    Counts all items in a single pass.
    """
    counts = Counter(data_list)
    return [(item, count) for item, count in counts.items()]


def efficient_file_operations(filename, lines):
    """
    FAST: Opening file once and writing all lines.
    Minimizes I/O operations.
    """
    with open(filename, 'a') as f:
        f.writelines(line + '\n' for line in lines)


def compute_factorials_with_cache(n, cache=None):
    """
    FAST: Iterative approach with caching.
    """
    if cache is None:
        cache = {}
    
    if n in cache:
        return cache[n]
    
    if n <= 1:
        result = 1
    else:
        result = n * compute_factorials_with_cache(n - 1, cache)
    
    cache[n] = result
    return result


def get_all_factorials(max_n):
    """
    FAST: Computing factorials iteratively, reusing previous results.
    """
    if max_n < 1:
        return []
    
    result = [1]  # 0! and 1! = 1
    current = 1
    
    for i in range(2, max_n + 1):
        current *= i
        result.append(current)
    
    return result


if __name__ == "__main__":
    print("Running optimized code demonstrations...")
    
    # Test 1: String concatenation
    start = time.time()
    result1 = efficient_string_concatenation(range(5000))
    print(f"String concatenation: {time.time() - start:.4f}s")
    
    # Test 2: List append
    start = time.time()
    result2 = efficient_list_append(5000)
    print(f"List append: {time.time() - start:.4f}s")
    
    # Test 3: Redundant computation
    start = time.time()
    data = ["Apple", "BANANA", "cherry", "APPLE", "banana"] * 1000
    result3 = efficient_computation_in_loop(data, "apple")
    print(f"Efficient computation: {time.time() - start:.4f}s")
    
    # Test 4: Nested loops
    start = time.time()
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    result4 = efficient_nested_loop_search(list1, list2)
    print(f"Set intersection: {time.time() - start:.4f}s")
    
    # Test 5: Multiple filtering
    start = time.time()
    numbers = list(range(-100, 200))
    result5 = efficient_filtering(numbers)
    print(f"Single-pass filtering: {time.time() - start:.4f}s")
    
    # Test 6: Dictionary lookup
    start = time.time()
    data_list = ['a', 'b', 'c', 'a', 'b', 'c'] * 100
    result6 = efficient_dictionary_lookup(data_list)
    print(f"Counter lookup: {time.time() - start:.4f}s")
    
    # Test 7: Factorials
    start = time.time()
    result7 = get_all_factorials(100)
    print(f"Iterative factorials: {time.time() - start:.4f}s")
