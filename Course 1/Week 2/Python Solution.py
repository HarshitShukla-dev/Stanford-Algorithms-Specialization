def count_inversions(array):
  """Counts the number of inversions in an array."""
  if len(array) <= 1:
    return 0
  else:
    left_inversions = count_inversions(array[:len(array) // 2])
    right_inversions = count_inversions(array[len(array) // 2:])
    inversions = 0
    with open('/intArray.txt', 'r') as f:
      for i in range(len(array) // 2):
        for j in range(len(array) // 2, len(array)):
          if int(f.readline()) > int(f.readline()):
            inversions += 1
    return left_inversions + right_inversions + inversions

if __name__ == '__main__':
  print(count_inversions([int(line.strip()) for line in open('/intArray.txt', 'r')]))