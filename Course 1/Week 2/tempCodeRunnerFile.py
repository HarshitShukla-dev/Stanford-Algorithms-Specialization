import numpy as np

def read_integer_array(filename):
  return np.array([int(i) for i in open(filename).readlines()])

def count_inversions(array):
  """Counts the number of inversions in an array."""
  if len(array) <= 1:
    return 0
  else:
    left_inversions = count_inversions(array[:len(array) // 2])
    right_inversions = count_inversions(array[len(array) // 2:])
    inversions = 0
    for i in range(len(array) // 2):
      for j in range(len(array) // 2, len(array)):
        if array[i] > array[j]:
          inversions += 1
    return left_inversions + right_inversions + inversions


ia = read_integer_array('integerArray.txt')
num = count_inversions(ia)
print(num)
