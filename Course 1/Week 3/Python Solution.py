class QuickSorter:
    def __init__(self, input_file=None):
        """
        Initialize the QuickSorter object.

        :param input_file: Optional. Name of the input file to read the array from.
        """
        self._comparisons = 0
        self._array = []
        self.read_input(input_file)

    @property
    def comparisons(self):
        """
        Get the number of comparisons performed during sorting.

        :return: Number of comparisons.
        """
        return self._comparisons

    @property
    def array(self):
        """
        Get the current array.

        :return: The array being sorted.
        """
        return self._array

    @array.setter
    def array(self, arr):
        """
        Set the array to be sorted.

        :param arr: The array to be sorted.
        """
        self._array = arr

    def read_input(self, input_file=None):
        """
        Read the input from a file or stdin and populate the array.

        :param input_file: Optional. Name of the input file to read the array from.
        """
        if input_file is None:
            self._array = [int(elem) for elem in input().split()]
        else:
            with open(input_file) as numbers:
                for number in numbers:
                    self._array.append(int(number))

    def sort(self):
        """
        Perform the quick sort algorithm on the array.
        """
        if len(self._array) <= 1:
            return
        self._qsort(0, len(self._array) - 1)

    def _qsort(self, start, end):
        """
        Recursive helper function for quick sort.

        :param start: Start index of the partition.
        :param end: End index of the partition.
        """
        if start >= end:
            return
        pivot = self.partition(start, end)
        self._qsort(start, pivot - 1)
        self._qsort(pivot + 1, end)

    def partition(self, start, end):
        """
        Partition the array and return the pivot index.

        :param start: Start index of the partition.
        :param end: End index of the partition.
        :return: Pivot index.
        """
        self._comparisons += end - start
        pivot = start
        for i in range(start + 1, end + 1):
            if self._array[i] < self._array[start]:
                pivot += 1
                self._array[i], self._array[pivot] = self._array[pivot], self._array[i]
        self._array[start], self._array[pivot] = self._array[pivot], self._array[start]
        return pivot


class QuickSorterFirstElementPivot(QuickSorter):
    """
    QuickSorter using the first element as the pivot.
    """

    def partition(self, start, end):
        """
        Override partition method to use the first element as the pivot.

        :param start: Start index of the partition.
        :param end: End index of the partition.
        :return: Pivot index.
        """
        return super().partition(start, end)


class QuickSorterLastElementPivot(QuickSorter):
    """
    QuickSorter using the last element as the pivot.
    """

    def partition(self, start, end):
        """
        Override partition method to use the last element as the pivot.

        :param start: Start index of the partition.
        :param end: End index of the partition.
        :return: Pivot index.
        """
        self._array[start], self._array[end] = self._array[end], self._array[start]
        return super().partition(start, end)


class QuickSorterMedianElementPivot(QuickSorter):
    """
    QuickSorter using the median element as the pivot.
    """

    def partition(self, start, end):
        """
        Override partition method to use the median element as the pivot.

        :param start: Start index of the partition.
        :param end: End index of the partition.
        :return: Pivot index.
        """
        self._choose_median_pivot(start, end)
        return super().partition(start, end)

    def _choose_median_pivot(self, start, end):
        """
        Choose the median element as the pivot and place it at the start of the array.

        :param start: Start index of the partition.
        :param end: End index of the partition.
        """
        length = end - start + 1
        median_index = length // 2 - 1 if length % 2 == 0 else length // 2
        median = start + median_index
        if self._array[start] <= self._array[median] <= self._array[end] or self._array[end] <= self._array[median] <= self._array[start]:
            self._array[start], self._array[median] = self._array[median], self._array[start]
        elif self._array[median] <= self._array[end] <= self._array[start] or self._array[start] <= self._array[end] <= self._array[median]:
            self._array[start], self._array[end] = self._array[end], self._array[start]


if __name__ == '__main__':
    # Create instances of each QuickSorter subclass and perform sorting
    sorters = (QuickSorterFirstElementPivot('intArray.txt'),
               QuickSorterLastElementPivot('intArray.txt'),
               QuickSorterMedianElementPivot('intArray.txt'))

    for sorter in sorters:
        sorter.sort()

    # Print the number of comparisons for each sorting method
    print(f"First Element Pivot Comparisons: {sorters[0].comparisons}")
    print(f"Last Element Pivot Comparisons: {sorters[1].comparisons}")
    print(f"Median Element Pivot Comparisons: {sorters[2].comparisons}")

# Output 162085 164123 138382