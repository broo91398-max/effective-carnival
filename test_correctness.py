"""
Unit tests to verify that slow and optimized code produce identical results.
"""

import unittest
import tempfile
import os
from slow_code import (
    inefficient_string_concatenation,
    inefficient_list_append,
    redundant_computation_in_loop,
    nested_loop_search,
    inefficient_filtering,
    inefficient_dictionary_lookup,
    inefficient_file_operations,
    get_all_factorials as slow_factorials,
)
from optimized_code import (
    efficient_string_concatenation,
    efficient_list_append,
    efficient_computation_in_loop,
    efficient_nested_loop_search,
    efficient_filtering,
    efficient_dictionary_lookup,
    efficient_file_operations,
    compute_factorials_with_cache,
    get_all_factorials as fast_factorials,
)


class TestCorrectness(unittest.TestCase):
    """Verify that optimized versions produce the same results as slow versions."""
    
    def test_string_concatenation(self):
        """Test string concatenation produces same result."""
        items = list(range(100))
        slow_result = inefficient_string_concatenation(items)
        fast_result = efficient_string_concatenation(items)
        self.assertEqual(slow_result, fast_result)
    
    def test_list_append(self):
        """Test list building produces same result."""
        n = 50
        slow_result = inefficient_list_append(n)
        fast_result = efficient_list_append(n)
        self.assertEqual(slow_result, fast_result)
    
    def test_redundant_computation(self):
        """Test search with redundant computation produces same result."""
        data = ["Apple", "BANANA", "cherry", "APPLE", "banana"]
        slow_result = redundant_computation_in_loop(data, "apple")
        fast_result = efficient_computation_in_loop(data, "apple")
        # Sort for comparison since order might differ
        self.assertEqual(sorted(slow_result), sorted(fast_result))
    
    def test_nested_loop_search(self):
        """Test finding common elements produces same result."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        slow_result = nested_loop_search(list1, list2)
        fast_result = efficient_nested_loop_search(list1, list2)
        # Sort for comparison since order might differ
        self.assertEqual(sorted(slow_result), sorted(fast_result))
    
    def test_filtering(self):
        """Test filtering produces same result."""
        numbers = list(range(-50, 150))
        slow_result = inefficient_filtering(numbers)
        fast_result = efficient_filtering(numbers)
        self.assertEqual(slow_result, fast_result)
    
    def test_dictionary_lookup(self):
        """Test counting elements produces same result."""
        data_list = ['a', 'b', 'c', 'a', 'b', 'c']
        slow_result = inefficient_dictionary_lookup(data_list)
        fast_result = efficient_dictionary_lookup(data_list)
        # Convert to dicts for comparison since order might differ
        slow_dict = dict(slow_result)
        fast_dict = dict(fast_result)
        self.assertEqual(slow_dict, fast_dict)
    
    def test_file_operations(self):
        """Test file operations produce same result."""
        lines = ['line1', 'line2', 'line3']
        
        # Create temporary files for testing
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as slow_file:
            slow_filename = slow_file.name
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as fast_file:
            fast_filename = fast_file.name
        
        try:
            # Write using both methods
            inefficient_file_operations(slow_filename, lines)
            efficient_file_operations(fast_filename, lines)
            
            # Read and compare results
            with open(slow_filename, 'r') as f:
                slow_content = f.read()
            
            with open(fast_filename, 'r') as f:
                fast_content = f.read()
            
            self.assertEqual(slow_content, fast_content)
        finally:
            # Clean up temporary files
            os.unlink(slow_filename)
            os.unlink(fast_filename)
    
    def test_cached_factorials(self):
        """Test cached factorial function produces correct results."""
        # Test individual factorials with cache
        cache = {}
        self.assertEqual(compute_factorials_with_cache(5, cache), 120)
        self.assertEqual(compute_factorials_with_cache(10, cache), 3628800)
        
        # Verify cache is being used (10! should be in cache from previous call)
        self.assertIn(10, cache)
        self.assertEqual(cache[10], 3628800)
    
    def test_factorials(self):
        """Test factorial computation produces same result."""
        n = 20
        slow_result = slow_factorials(n)
        fast_result = fast_factorials(n)
        self.assertEqual(slow_result, fast_result)
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Empty inputs
        self.assertEqual(
            inefficient_string_concatenation([]),
            efficient_string_concatenation([])
        )
        self.assertEqual(
            inefficient_list_append(0),
            efficient_list_append(0)
        )
        self.assertEqual(
            nested_loop_search([], [1, 2, 3]),
            efficient_nested_loop_search([], [1, 2, 3])
        )
        
        # Single element
        self.assertEqual(
            inefficient_string_concatenation([42]),
            efficient_string_concatenation([42])
        )


if __name__ == '__main__':
    unittest.main()
