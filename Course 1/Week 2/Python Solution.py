def merge(left, right):
    """
    Merges two sorted arrays and returns the merged array and the number of inversions.

    Args:
        left: The left sorted array.
        right: The right sorted array.

    Returns:
        The merged array and the number of inversions.
    """

    inversions = 0
    result = []
    i, j = 0, 0
    left_len = len(left)
    right_len = len(right)
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            inversions += left_len - i
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result, inversions


def mergesort(lst):
    """
    Sorts the given array using the merge sort algorithm and returns the sorted array and the number of inversions.

    Args:
        lst: The array to be sorted.

    Returns:
        The sorted array and the number of inversions.
    """

    if len(lst) <= 1:
        return lst, 0

    middle = int(len(lst) / 2)
    (left, x) = mergesort(lst[:middle])
    (right, y) = mergesort(lst[middle:])
    (combined, z) = merge(left, right)
    return combined, x + y + z


def main():
    """
    Reads the input file and prints the number of inversions.
    """

    with open("integerArray.txt") as f:
        lines = []
        for line in f:
            lines.append(int(line))

    (sorted_lines, inversions) = mergesort(lines)
    print(inversions)


if __name__ == "__main__":
    main()
