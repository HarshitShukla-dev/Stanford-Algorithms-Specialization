"""
Inversions: num of (i, j) in A where i<j and A[i]>A[j]
"""

def read_integer_array(filename):
  with open(filename, 'r') as f:
    ls = f.readlines()
  return [int(i) for i in ls]

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
