# This is a sample Python script.
from sorting.bubbleSort import BubbleSort
from sorting.insertionSort import InsertionSort
from sorting.selectionSort import SelectionSort
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def printPattern(n):
    k = 2 * n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i):
            print("*", end=" ")
        print("\r")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #ls = [20, 35, -15, 7, 55, 1, -22]
    #print("List before Bubble Sort : ",ls)
    #bs = BubbleSort()
    #bs.bsort(ls)
    #print("List after Bubble Sort : ", ls)
    ls = [20, 35, -15, 7, 55, 1, -22]
    print("List before Selection Sort : ", ls)
    ls = [20, 35, -15, 7, 55, 1, -22]
    sel=SelectionSort()
    sel.selectionSort(ls)
    print("List after Selection Sort : ", ls)
    #ls = [20, 35, -15, 7, 55, 1, -22]
    #print("List before Insertion Sort : ", ls)
    #ins=InsertionSort()
    #ins.insertionSort(ls)
    #sprint("List after Insertion Sort : ", ls)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
