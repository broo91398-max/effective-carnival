"""
Performance benchmark comparing slow vs optimized code.
"""

import time
import sys
from slow_code import (
    inefficient_string_concatenation,
    inefficient_list_append,
    redundant_computation_in_loop,
    nested_loop_search,
    inefficient_filtering,
    inefficient_dictionary_lookup,
    get_all_factorials as slow_factorials,
)
from optimized_code import (
    efficient_string_concatenation,
    efficient_list_append,
    efficient_computation_in_loop,
    efficient_nested_loop_search,
    efficient_filtering,
    efficient_dictionary_lookup,
    get_all_factorials as fast_factorials,
)


def benchmark_function(func, *args, **kwargs):
    """Run a function multiple times and return average execution time."""
    iterations = kwargs.pop('iterations', 5)
    times = []
    
    for _ in range(iterations):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        times.append(end - start)
    
    return sum(times) / len(times)


def print_comparison(name, slow_time, fast_time):
    """Print formatted comparison of execution times."""
    speedup = slow_time / fast_time if fast_time > 0 else float('inf')
    percentage = ((slow_time - fast_time) / slow_time * 100) if slow_time > 0 else 0
    
    print(f"\n{name}:")
    print(f"  Slow version: {slow_time:.6f}s")
    print(f"  Fast version: {fast_time:.6f}s")
    print(f"  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {percentage:.1f}% faster")


def main():
    """Run all benchmarks and display results."""
    print("=" * 60)
    print("Performance Benchmark: Slow vs Optimized Code")
    print("=" * 60)
    
    # Benchmark 1: String concatenation
    items = list(range(5000))
    slow_time = benchmark_function(inefficient_string_concatenation, items)
    fast_time = benchmark_function(efficient_string_concatenation, items)
    print_comparison("String Concatenation", slow_time, fast_time)
    
    # Benchmark 2: List operations
    n = 5000
    slow_time = benchmark_function(inefficient_list_append, n)
    fast_time = benchmark_function(efficient_list_append, n)
    print_comparison("List Building", slow_time, fast_time)
    
    # Benchmark 3: Redundant computation
    data = ["Apple", "BANANA", "cherry", "APPLE", "banana"] * 1000
    slow_time = benchmark_function(redundant_computation_in_loop, data, "apple")
    fast_time = benchmark_function(efficient_computation_in_loop, data, "apple")
    print_comparison("Loop with Redundant Computation", slow_time, fast_time)
    
    # Benchmark 4: Nested loops
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    slow_time = benchmark_function(nested_loop_search, list1, list2)
    fast_time = benchmark_function(efficient_nested_loop_search, list1, list2)
    print_comparison("Finding Common Elements", slow_time, fast_time)
    
    # Benchmark 5: Multiple filtering passes
    numbers = list(range(-100, 200))
    slow_time = benchmark_function(inefficient_filtering, numbers)
    fast_time = benchmark_function(efficient_filtering, numbers)
    print_comparison("Multiple Filter Operations", slow_time, fast_time)
    
    # Benchmark 6: Dictionary operations
    data_list = ['a', 'b', 'c', 'a', 'b', 'c'] * 100
    slow_time = benchmark_function(inefficient_dictionary_lookup, data_list)
    fast_time = benchmark_function(efficient_dictionary_lookup, data_list)
    print_comparison("Counting Elements", slow_time, fast_time)
    
    # Benchmark 7: Factorial computation
    n = 100
    slow_time = benchmark_function(slow_factorials, n)
    fast_time = benchmark_function(fast_factorials, n)
    print_comparison("Computing Factorials", slow_time, fast_time)
    
    print("\n" + "=" * 60)
    print("Benchmark complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
