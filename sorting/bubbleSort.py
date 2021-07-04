class BubbleSort:

    def swap(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def bsort(self, intArray):
        for unSortedIndex in range(len(intArray) - 1, -1, -1):
            for i in range(0, unSortedIndex):
                if intArray[i] > intArray[i + 1]:
                    self.swap(intArray, i, i + 1)
