"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot = 0
    leftmark = 1
    rightmark = len(array) - 1
    while leftmark < rightmark:
        print array
        if array[leftmark] <= array[pivot]:
            while leftmark < rightmark:
                if array[pivot] <= array[rightmark]:
                    rightmark -= 1
                if array[pivot] > array[rightmark]:
                    print array
                    temp = array[rightmark]
                    array[rightmark] = array[leftmark]
                    array[leftmark] = temp
                    rightmark -= 1
        if array[leftmark] >= array[pivot]:
            leftmark += 1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
