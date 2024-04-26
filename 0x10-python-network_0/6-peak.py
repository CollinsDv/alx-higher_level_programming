#!/usr/bin/python3
"""
module: 6-peak
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): List of unsorted integers.
    Returns:
        int: A peak integer.
    """
    if not list_of_integers:
        return None

    # Function to check if a given index is a peak
    def is_peak(index):
        if index == 0:
            return list_of_integers[index] >= list_of_integers[index + 1]
        if index == len(list_of_integers) - 1:
            return list_of_integers[index] >= list_of_integers[index - 1]
        return list_of_integers[index] >= list_of_integers[
                index - 1] and list_of_integers[
                        index] >= list_of_integers[index + 1]

    # Binary search to find a peak
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if is_peak(mid):
            return list_of_integers[mid]
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    # Check if the last remaining element is a peak
    if is_peak(left):
        return list_of_integers[left]

    return None
