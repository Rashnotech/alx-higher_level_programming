#!/usr/bin/python3
"""a module that find a peak"""


def find_peak(arr):
    """
        a function that finds a peak in a list of unsorted integers
        Args:
            arr: an array of unsorted integers
        Returns:
            function returns peak in the list of integers
    """
    if not arr:
        return None

    size = len(arr)
    for i in range(size):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]
    else:
        return None
