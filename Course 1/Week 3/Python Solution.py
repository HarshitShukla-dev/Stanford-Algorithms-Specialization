class QuickSorter:
    """
    A quicksort implementation.

    Attributes:
        comparisons (int): The number of comparisons made by the algorithm.
        array (list): The array to be sorted.

    Methods:
        read_input(input_file=None): Reads the input from a file or the console.
        sort(): Sorts the array.
        partition(start, end): Partitions the array around the pivot element.
    """

    def __init__(self, input_file=None):
        self.comparisons = 0
        self.array = []
        self.read_input(input_file)

    @property
    def comparisons(self):
        """The number of comparisons made by the algorithm."""
        return self._comparisons

    @property
    def array(self):
        """The array to be sorted."""
        return self._array

    @array.setter
    def array(self, arr):
        """Sets the array to be sorted."""
        self._array = arr

    def read_input(self, input_file=None):
        """Reads the input from a file or the console."""
        if input_file is None:
            self.array = [int(elem) for elem in input().split()]
            return
        with open(input_file) as numbers:
            for number in numbers:
                self.array.append(int(number))

    def sort(self):
        """Sorts the array."""
        if len(self.array) <= 1:
            return
        self._qsort(0, len(self.array) - 1)

    def _qsort(self, start, end):
        """Recursively sorts the array."""
        if start >= end:
            return
        pivot = self.partition(start, end)
        self._qsort(start, pivot - 1)
        self._qsort(pivot + 1, end)

    def partition(self, start, end):
        """Partitions the array around the pivot element."""
        self.comparisons += end - start
        pivot = start
        for i in range(start + 1, end + 1):
            if self.array[i] < self.array[start]:
                pivot += 1
                self.array[i], self.array[pivot] = self.array[pivot], self.array[i]
        self.array[start], self.array[pivot] = self.array[pivot], self.array[start]
        return pivot


def main():
    """Sorts the input array and prints the number of comparisons made."""
    sorters = (QuickSorter('intArray.txt'),
               QuickSorter('intArray.txt'),
               QuickSorter('intArray.txt'))
    for sorter in sorters:
        sorter.sort()
    print(sorters[0].comparisons, sorters[1].comparisons, sorters[2].comparisons)


if __name__ == '__main__':
    main()
