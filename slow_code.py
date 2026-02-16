"""
Demonstration of slow and inefficient code patterns.
This file intentionally contains performance anti-patterns for educational purposes.
"""

import time


def inefficient_string_concatenation(items):
    """
    SLOW: Using string concatenation in a loop.
    Each concatenation creates a new string object.
    """
    result = ""
    for item in items:
        result = result + str(item) + ","
    return result[:-1] if result else ""


def inefficient_list_append(n):
    """
    SLOW: Creating new lists repeatedly instead of appending.
    Each addition creates a new list object.
    """
    result = []
    for i in range(n):
        result = result + [i * i]
    return result


def redundant_computation_in_loop(data, search_term):
    """
    SLOW: Performing the same computation repeatedly in a loop.
    The upper() call on search_term happens every iteration.
    """
    matches = []
    for item in data:
        if item.upper() == search_term.upper():
            matches.append(item)
    return matches


def nested_loop_search(list1, list2):
    """
    SLOW: Nested loops for membership checking - O(n*m) complexity.
    """
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
    return common


def inefficient_filtering(numbers):
    """
    SLOW: Multiple passes through the same list.
    Each filter operation creates a new list.
    """
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    
    temp = []
    for num in result:
        if num % 2 == 0:
            temp.append(num)
    
    final = []
    for num in temp:
        if num < 100:
            final.append(num)
    
    return final


def inefficient_dictionary_lookup(data_list):
    """
    SLOW: Repeated linear searches instead of using a dictionary.
    """
    result = []
    for item in data_list:
        count = 0
        for other_item in data_list:
            if item == other_item:
                count += 1
        result.append((item, count))
    return result


def inefficient_file_operations(filename, lines):
    """
    SLOW: Opening and closing file repeatedly in a loop.
    """
    for line in lines:
        with open(filename, 'a') as f:
            f.write(line + '\n')


def compute_factorials_recursively(n):
    """
    SLOW: Recursive without memoization, redundant calculations.
    
    Note: Returns 1 for both 0! and 1! (mathematically correct).
          However, get_all_factorials() returns factorials starting from 1!,
          not including 0!, to match typical use cases.
    """
    if n <= 1:
        return 1
    return n * compute_factorials_recursively(n - 1)


def get_all_factorials(max_n):
    """
    SLOW: Computing factorials from scratch each time.
    
    Args:
        max_n: Compute factorials from 1! up to max_n!
    
    Returns:
        List of factorials [1!, 2!, ..., max_n!]
        Returns empty list if max_n < 1
        
    Note: This function returns factorials starting from 1!, not 0!.
    """
    result = []
    for i in range(1, max_n + 1):
        result.append(compute_factorials_recursively(i))
    return result


if __name__ == "__main__":
    print("Running slow code demonstrations...")
    
    # Test 1: String concatenation
    start = time.time()
    result1 = inefficient_string_concatenation(range(5000))
    print(f"String concatenation: {time.time() - start:.4f}s")
    
    # Test 2: List append
    start = time.time()
    result2 = inefficient_list_append(5000)
    print(f"List append: {time.time() - start:.4f}s")
    
    # Test 3: Redundant computation
    start = time.time()
    data = ["Apple", "BANANA", "cherry", "APPLE", "banana"] * 1000
    result3 = redundant_computation_in_loop(data, "apple")
    print(f"Redundant computation: {time.time() - start:.4f}s")
    
    # Test 4: Nested loops
    start = time.time()
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    result4 = nested_loop_search(list1, list2)
    print(f"Nested loops: {time.time() - start:.4f}s")
    
    # Test 5: Multiple filtering
    start = time.time()
    numbers = list(range(-100, 200))
    result5 = inefficient_filtering(numbers)
    print(f"Multiple filtering: {time.time() - start:.4f}s")
    
    # Test 6: Dictionary lookup
    start = time.time()
    data_list = ['a', 'b', 'c', 'a', 'b', 'c'] * 100
    result6 = inefficient_dictionary_lookup(data_list)
    print(f"Dictionary lookup: {time.time() - start:.4f}s")
    
    # Test 7: Factorials
    start = time.time()
    result7 = get_all_factorials(100)
    print(f"Factorials: {time.time() - start:.4f}s")
