class SelectionSort:

    def swap(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def selectionSort(self,intArray):
        for unsortedIndex in range(len(intArray)-1,-1,-1):
            largestIndex=0
            for i in range(0,unsortedIndex+1):
                if intArray[i]>intArray[largestIndex]:
                    largestIndex=i
            self.swap(intArray,largestIndex,unsortedIndex)
