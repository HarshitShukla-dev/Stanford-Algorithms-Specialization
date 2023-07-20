import random

comparisons = 0

def read_input(input_file=None):
    if input_file is None:
        return [int(elem) for elem in input().split()]
    else:
        with open(input_file) as numbers:
            return [int(number) for number in numbers]

def quick_sort(arr):
    global comparisons
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]

    comparisons += len(arr) - 1
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_first_pivot(arr):
    global comparisons
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    comparisons += len(arr) - 1
    return quick_sort_first_pivot(left) + [pivot] + quick_sort_first_pivot(right)

def quick_sort_last_pivot(arr):
    global comparisons
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    comparisons += len(arr) - 1
    return quick_sort_last_pivot(left) + [pivot] + quick_sort_last_pivot(right)

def quick_sort_median_pivot(arr):
    global comparisons
    if len(arr) <= 1:
        return arr

    median_index = len(arr) // 2
    pivot_candidates = [arr[0], arr[-1], arr[median_index]]
    pivot_candidates.sort()
    pivot = pivot_candidates[1]

    left = [x for i, x in enumerate(arr) if x < pivot and i != median_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != median_index]

    comparisons += len(arr) - 1
    return quick_sort_median_pivot(left) + [pivot] + quick_sort_median_pivot(right)

if __name__ == '__main__':
    input_array = read_input('intArray.txt')
    comparisons = 0

    sorted_array = quick_sort(input_array.copy())
    print(f"Random Pivot Comparisons: {comparisons}")

    comparisons = 0
    sorted_array_first_pivot = quick_sort_first_pivot(input_array.copy())
    print(f"First Element Pivot Comparisons: {comparisons}")

    comparisons = 0
    sorted_array_last_pivot = quick_sort_last_pivot(input_array.copy())
    print(f"Last Element Pivot Comparisons: {comparisons}")

    comparisons = 0
    sorted_array_median_pivot = quick_sort_median_pivot(input_array.copy())
    print(f"Median Element Pivot Comparisons: {comparisons}")
