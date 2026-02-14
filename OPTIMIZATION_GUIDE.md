# Performance Optimization Guide

This document provides detailed explanations of the performance issues identified in this project and their solutions.

## Table of Contents
1. [String Concatenation](#1-string-concatenation)
2. [List Building](#2-list-building)
3. [Redundant Computations](#3-redundant-computations)
4. [Nested Loops](#4-nested-loops)
5. [Multiple Passes](#5-multiple-passes)
6. [Dictionary Operations](#6-dictionary-operations)
7. [Recursive Calculations](#7-recursive-calculations)

---

## 1. String Concatenation

### Problem
```python
result = ""
for item in items:
    result = result + str(item) + ","
```

**Why it's slow**: In Python, strings are immutable. Each concatenation creates a new string object and copies all previous content. For n items, this results in O(n²) complexity.

### Solution
```python
result = ",".join(str(item) for item in items)
```

**Why it's fast**: The `join()` method allocates memory once based on the total size needed, then fills it in a single pass - O(n) complexity.

**Performance gain**: 7-100x faster (scales with data size)

---

## 2. List Building

### Problem
```python
result = []
for i in range(n):
    result = result + [i * i]
```

**Why it's slow**: Similar to strings, each `+` operation creates a new list and copies all existing elements - O(n²) complexity.

### Solution
```python
result = [i * i for i in range(n)]
# or
result = []
for i in range(n):
    result.append(i * i)
```

**Why it's fast**: List comprehensions are optimized at the C level. The `append()` method amortizes cost by pre-allocating extra space - O(n) complexity.

**Performance gain**: 113x faster in benchmarks

---

## 3. Redundant Computations

### Problem
```python
for item in data:
    if item.upper() == search_term.upper():  # upper() called n times
        matches.append(item)
```

**Why it's slow**: `search_term.upper()` is computed repeatedly even though it never changes.

### Solution
```python
search_upper = search_term.upper()  # Compute once
for item in data:
    if item.upper() == search_upper:
        matches.append(item)
```

**Why it's fast**: Loop-invariant code is moved outside the loop, reducing function calls from n to 1.

**Performance gain**: 1.85x faster

**General rule**: Any computation that doesn't depend on the loop variable should be done before the loop.

---

## 4. Nested Loops

### Problem
```python
common = []
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common.append(item1)
```

**Why it's slow**: For every element in list1, we scan all of list2 - O(n×m) complexity.

### Solution
```python
common = list(set(list1) & set(list2))
```

**Why it's fast**: Converting to sets allows O(1) membership testing. Total complexity is O(n+m) - just the time to process each list once.

**Performance gain**: 306x faster in benchmarks

**Trade-off**: Sets use more memory and don't preserve order or duplicates. If those matter, use a set for the lookup but iterate differently:

```python
set2 = set(list2)
common = [item for item in list1 if item in set2]
```

---

## 5. Multiple Passes

### Problem
```python
result = [num for num in numbers if num > 0]
result = [num for num in result if num % 2 == 0]
result = [num for num in result if num < 100]
```

**Why it's slow**: Three separate iterations over the data, creating intermediate lists.

### Solution
```python
result = [num for num in numbers 
          if num > 0 and num % 2 == 0 and num < 100]
```

**Why it's fast**: Single pass through the data with combined conditions.

**Performance gain**: 1.3x faster

**When to use**: Combine filters when possible. Separate them only when:
- Early filters significantly reduce data size
- Different filters are used in different contexts
- Readability is significantly impaired

---

## 6. Dictionary Operations

### Problem
```python
for item in data_list:
    count = 0
    for other_item in data_list:
        if item == other_item:
            count += 1
    result.append((item, count))
```

**Why it's slow**: For each unique item, we scan the entire list - O(n²) complexity.

### Solution
```python
from collections import Counter
counts = Counter(data_list)
result = list(counts.items())
```

**Why it's fast**: Counter makes a single pass through the data - O(n) complexity.

**Performance gain**: 272x faster in benchmarks

**General principle**: Use hash tables (dicts/sets) for lookups and counting. Python's built-in `Counter`, `defaultdict`, and `set` are highly optimized.

---

## 7. Recursive Calculations

### Problem
```python
def compute_factorials_recursively(n):
    if n <= 1:
        return 1
    return n * compute_factorials_recursively(n - 1)

# Computing factorials 1! through 100!
for i in range(1, 101):
    result.append(compute_factorials_recursively(i))
```

**Why it's slow**: Each factorial is computed from scratch. Computing 100! requires computing 99!, 98!, ... 1! every time.

### Solution
```python
def get_all_factorials(max_n):
    result = [1]
    current = 1
    for i in range(2, max_n + 1):
        current *= i
        result.append(current)
    return result
```

**Why it's fast**: Each factorial reuses the previous result. Only one multiplication per number.

**Performance gain**: 48x faster

**General principles**:
- Avoid redundant calculations - cache results (memoization)
- Prefer iteration over recursion when possible (no call stack overhead)
- Recognize when a problem has overlapping subproblems (dynamic programming)

---

## General Best Practices

### 1. Profile Before Optimizing
- Use `cProfile` or `timeit` to find actual bottlenecks
- Don't optimize code that isn't slow
- Focus on the 20% of code that takes 80% of the time

### 2. Choose the Right Data Structure
- **Lists**: Sequential access, dynamic arrays
- **Sets**: Fast membership testing, unique elements
- **Dicts**: Fast key-value lookups
- **Deques**: Fast insertion/deletion at both ends
- **Arrays**: Memory-efficient for numeric data

### 3. Use Built-in Functions
Python's built-ins are implemented in C and highly optimized:
- `sum()`, `min()`, `max()`, `all()`, `any()`
- `map()`, `filter()` (though comprehensions are often clearer)
- `sorted()`, `reversed()`

### 4. Leverage Comprehensions
List/dict/set comprehensions are faster than equivalent loops:
```python
# Fast
squares = [x*x for x in range(100)]

# Slower
squares = []
for x in range(100):
    squares.append(x*x)
```

### 5. Consider Generator Expressions
For large datasets that don't need to be stored entirely in memory:
```python
# Memory efficient
sum(x*x for x in range(1000000))

# Uses lots of memory
sum([x*x for x in range(1000000)])
```

### 6. Avoid Global Variables
Global variable lookups are slower than local variables.

### 7. Use `__slots__` for Classes with Many Instances
Reduces memory usage and attribute access time.

---

## Measuring Performance

### Using timeit
```python
import timeit

# Time a small snippet
time = timeit.timeit('sum(range(100))', number=10000)
print(f"Time: {time:.6f} seconds")
```

### Using cProfile
```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Your code here

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumtime')
stats.print_stats(10)  # Top 10 functions
```

### Using time.time()
```python
import time

start = time.time()
# Your code here
end = time.time()
print(f"Elapsed: {end - start:.6f} seconds")
```

---

## When NOT to Optimize

- Code that runs infrequently
- Code that's already fast enough
- Before you have a working implementation
- When it significantly hurts readability
- When the performance gain is negligible

**Remember**: "Premature optimization is the root of all evil" - Donald Knuth

Focus on:
1. Correctness first
2. Clarity second  
3. Performance third (and only when needed)
