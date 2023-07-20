"""
Inversions: num of (i, j) in A where i<j and A[i]>A[j]
"""

ia = []
f = open('intArray.txt', 'r')
ls = f.readlines()
f.close()
ia = [int(i) for i in ls]


def count_inversions(array):
  """Counts the number of inversions in an array."""
  if len(array) <= 1:
    return 0
  else:
    left_inversions = count_inversions(array[:len(array) // 2])
    right_inversions = count_inversions(array[len(array) // 2:])
    inversions = 0
    with open('integerarray.txt', 'r') as f:
      for i in range(len(array) // 2):
        for j in range(len(array) // 2, len(array)):
          if int(f.readline()) > int(f.readline()):
            inversions += 1
    return left_inversions + right_inversions + inversions


_, num = count_inversions(ia)
print(num)