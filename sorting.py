# A collection of sorting algorithms written in python

# Classic bubble sort. A pretty bad but staple alg
def bubble_sort(arr):
    end = len(arr)

    while end > 0:
        newend = 0
        for i in range(1, end):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                newend = i
        end = newend


# Insertion sort. Not awesome but better than bubble
def insertion_sort(arr):
    for i in range(0, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Quick sort. Cool and quick
def quick_sort(arr, low = 0, high = None):
    if high == None:
        high = len(arr) - 1

    if low >= high:
        return arr

    pivot = arr[high]
    i = low 

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    quick_sort(arr, low, i - 1)
    quick_sort(arr, i + 1, high)


# Merge sort. A good staple, maybe a best
def merge_sort(arr):
    l = len(arr)
    if l < 2:
        return arr

    # Split arrays in half and sort
    half = l//2
    lhs = merge_sort(arr[:half])
    rhs = merge_sort(arr[half:])

    # Merge, taking the smallest element each time
    i, j, arr = 0, 0, []

    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:
            arr.append(lhs[i])
            i += 1
        else:
            arr.append(rhs[j])
            j += 1

    if i == len(lhs):
        for x in rhs[j:]:
            arr.append(x)
    else:
        for x in lhs[i:]:
            arr.append(x)

    return arr


# Testing
import unittest
from copy import deepcopy

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            [],
            [1],
            [1, 2, 3],
            [3, 2, 1],
            [5, 1, 4, 2, 8],
            [10, -1, 3, 5, -7, 0],
            [2, 3, 2, 3, 1, 1],
        ]

    def test_bubble_sort(self):
        for case in self.test_cases:
            arr = deepcopy(case)
            bubble_sort(arr)
            self.assertEqual(arr, sorted(case), f"Failed on input: {case}")
    
    def test_insertion_sort(self):
        for case in self.test_cases:
            arr = deepcopy(case)
            insertion_sort(arr)
            self.assertEqual(arr, sorted(case), f"Failed on input: {case}")

    def test_merge_sort(self):
        for case in self.test_cases:
            sorted_arr = merge_sort(case)
            self.assertEqual(sorted_arr, sorted(case), f"Failed on input: {case}")

    def test_quick_sort(self):
        for case in self.test_cases:
            arr = deepcopy(case)
            quick_sort(arr)
            self.assertEqual(arr, sorted(case), f"Failed on input: {case}")

if __name__ == '__main__':
    unittest.main()





#
