"""
Inversions: num of (i, j) in A where i<j and A[i]>A[j]
"""

ia = []
f = open(r'C:\Users\Administrator\Documents\Programming\Stanford-Algorithms-Specialization\Course 1\Week 2\integerArray.txt', 'r')
ls = f.readlines()
f.close()
ia = [int(i) for i in ls]
print(ls)

def count_inversions(array):
  """Counts the number of inversions in an array."""
  if len(array) <= 1:
    return 0
  else:
    left_inversions = count_inversions(array[:len(array) // 2])
    right_inversions = count_inversions(array[len(array) // 2:])
    inversions = 0
    with open(r'C:\Users\Administrator\Documents\Programming\Stanford-Algorithms-Specialization\Course 1\Week 2\integerArray.txt', 'r') as f:
      for i in range(len(array) // 2):
        for j in range(len(array) // 2, len(array)):
          if int(f.readline()) > int(f.readline()):
            inversions += 1
    return left_inversions + right_inversions + inversions


num = count_inversions(ia)
print(num)