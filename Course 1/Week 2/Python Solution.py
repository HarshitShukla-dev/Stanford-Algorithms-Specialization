def merge(left, right):
    inversions = 0
    result = []
    i, j = 0 , 0
    left_len = len(left)
    right_len = len(right)
    while i < left_len and j < right_len: # iterate through both arrays and arrange the elements in sorted order
        if left[i] <= right [j]:
            result.append(left[i])
            i+=1
        else:
            inversions += (left_len - i)
            result.append(right[j])
            j+=1

    result += left[i:]
    result += right[j:]
    return result, inversions

#The mergesort method to split the arrays into smaller subarrays
def mergesort(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int(len(lst) / 2)
    (left,x) = mergesort(lst[:middle])
    (right,y) = mergesort(lst[middle:])
    (combined, z) = merge(left, right)
    return combined, x+y+z

with open('integerArray.txt') as fp:
    lines = fp.read().split("\n")

(sorted_lines, inversions) = mergesort(lines)
print(inversions)

