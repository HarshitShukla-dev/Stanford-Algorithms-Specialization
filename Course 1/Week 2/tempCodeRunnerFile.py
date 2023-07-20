import numpy as np

def read_integer_array(filename):
  return np.array([int(i) for i in open(filename).readlines()])

def count_inversions_merge_sort(array):
  """Counts the number of inversions in an array using the merge sort algorithm."""
  if len(array) <= 1:
    return 0
  else:
    middle = len(array) // 2
    left_inversions = count_inversions_merge_sort(array[:middle])
    right_inversions = count_inversions_merge_sort(array[middle:])
    inversions = 0
    i = 0
    j = middle
    while i < middle and j < len(array):
      if array[i] > array[j]:
        inversions += middle - i
      elif array[i] == array[j]:
        inversions += 0
      else:
        inversions += 0
      i += 1
      j += 1
    return left_inversions + right_inversions + inversions


ia = read_integer_array('integerArray.txt')
num = count_inversions_merge_sort(ia)
print(num)
