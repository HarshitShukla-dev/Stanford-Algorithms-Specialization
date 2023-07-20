## Problem 1: Find the second-largest number in an unsorted array of n distinct numbers, where n is a power of 2.

```python
def find_second_largest(array):
  """Finds the second-largest number in an unsorted array of n distinct numbers, where n is a power of 2."""
  largest = max(array)
  array.remove(largest)
  second_largest = max(array)
  return second_largest```

## Problem 2: Find the maximum element in a unimodal array in O(log n) time.

```python
def find_maximum_in_unimodal_array(array):
  """Finds the maximum element in a unimodal array in O(log n) time."""
  middle = len(array) // 2
  if array[middle] > array[middle - 1]:
    return find_maximum_in_unimodal_array(array[:middle])
  else:
    return find_maximum_in_unimodal_array(array[middle:])

## Problem 3: Find an index i such that A[i] = i in a sorted array A of n distinct integers.

```python
def find_index_equal_to_value(array):
  """Finds an index i such that A[i] = i in a sorted array A of n distinct integers."""
  j = 0
  while j < len(array):
    if array[j] == j:
      return j
    else:
      j += 1
  return -1

## Problem 4: Find a local minimum in an n by n grid of distinct numbers with only O(n) comparisons between pairs of numbers.

```python
def find_local_minimum(grid):
  """Finds a local minimum in an n by n grid of distinct numbers with only O(n) comparisons between pairs of numbers."""
  min_value = grid[0]
  for i in range(len(grid)):
    if grid[i] < min_value:
      min_value = grid[i]
  return min_value
````
