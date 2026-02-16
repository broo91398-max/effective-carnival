# Effective Carnival - Performance Optimization Examples

A demonstration project showing common performance anti-patterns in Python code and their optimized solutions.

## Overview

This repository contains examples of slow, inefficient code patterns alongside their optimized versions. Each example demonstrates a specific performance issue and how to fix it.

## Files

- **slow_code.py** - Contains intentionally slow implementations demonstrating common performance anti-patterns
- **optimized_code.py** - Contains efficient implementations using best practices
- **benchmark.py** - Performance comparison script that measures the difference between slow and optimized code

## Performance Issues Addressed

### 1. String Concatenation in Loops
**Problem**: Using `+` operator to concatenate strings in a loop creates a new string object each time (O(n²) complexity).

**Solution**: Use `str.join()` with a generator/list (O(n) complexity).

**Improvement**: 10-100x faster depending on the number of strings.

### 2. List Building with Repeated Concatenation
**Problem**: Using `list = list + [item]` creates a new list object each iteration.

**Solution**: Use list comprehension or `append()` method.

**Improvement**: 50-200x faster for large lists.

### 3. Redundant Computations in Loops
**Problem**: Computing the same value repeatedly inside a loop when the value doesn't change.

**Solution**: Calculate invariant values once before the loop.

**Improvement**: 2-5x faster.

### 4. Nested Loops for Membership Testing
**Problem**: Using nested loops for finding common elements (O(n×m) complexity).

**Solution**: Use set intersection (O(n+m) complexity).

**Improvement**: 100-1000x faster for large datasets.

### 5. Multiple Passes Over Data
**Problem**: Filtering the same data multiple times with separate loops.

**Solution**: Combine conditions into a single pass.

**Improvement**: 3-5x faster.

### 6. Linear Search for Counting
**Problem**: Repeatedly searching through a list to count occurrences (O(n²) complexity).

**Solution**: Use `collections.Counter` (O(n) complexity).

**Improvement**: 100-500x faster.

### 7. Redundant Recursive Calculations
**Problem**: Computing factorials recursively without memoization, recalculating the same values.

**Solution**: Use iterative approach, reusing previous results.

**Improvement**: 10-50x faster.

## Running the Benchmarks

```bash
python benchmark.py
```

This will run performance comparisons between the slow and optimized versions of each function.

## Running Individual Examples

```bash
# Run slow implementations
python slow_code.py

# Run optimized implementations
python optimized_code.py
```

## Key Takeaways

1. **Use built-in functions**: Python's built-in functions and methods are implemented in C and highly optimized.
2. **Avoid unnecessary object creation**: Reuse objects when possible instead of creating new ones.
3. **Choose the right data structure**: Sets for membership testing, dicts for lookups, lists for sequential access.
4. **Minimize I/O operations**: Batch file operations instead of repeated open/close cycles.
5. **Hoist invariants out of loops**: Don't recompute values that don't change.
6. **Use comprehensions**: List/dict/set comprehensions are faster than equivalent loops.
7. **Consider algorithmic complexity**: O(n) algorithms scale much better than O(n²) ones.

## Requirements

- Python 3.6+
- No external dependencies required
