class InsertionSort:

    def insertionSort(self,intArray):
        for firstUnsortedIndex in range(1,len(intArray)):
            nextElement=intArray[firstUnsortedIndex]
            i=firstUnsortedIndex
            while i>0 and intArray[i-1]>nextElement:
                intArray[i]=intArray[i-1]
                i-=1
            intArray[i]=nextElement


