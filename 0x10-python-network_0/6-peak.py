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
    if size != 0:
        for i in range(size):
            x = i + 1
            if x != size-1:
                peak = arr[i] + arr[x]
                if peak == arr[x + 1]:
                    return arr[x + 1]
            else:
                return max(arr)
