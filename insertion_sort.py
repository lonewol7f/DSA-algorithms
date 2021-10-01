"""
Pseudocode for Insertion sort

insertion_sort(A)
    for j = 2 to A.length
        key = A[j]
        // Insert A[j] in to the sorted sequence
        i = j - 1
        While i > 0 and A[i] > key
            A[i + 1] = A[i]
            i = i -1
        A[i + 1] = key


* Best case - Array is in sorted order
    T(n) -> an + b  -> O(n)

* Worst case - Array is in reversed sorted order
    T(n) -> cn² + dn + e  -> O(n²)

|
* Run in Terminal: python3 insertion_sort.py <number list seperated by comma without spaces>
* Example: python3 insertion_sort.py 12,4,25,28,5

"""

import sys


def insertion_sort(a):
    """
    This algorithm use to sort number lists

    Args:
        a: Unsorted list of numbers

    Returns:
        Sorted list of numbers

    """
    for j in range(2, len(a)):
        key = a[j]
        # Insert a[j] into the sorted sequence
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

    return a


if __name__ == '__main__':
    str_number_list = (sys.argv[1].split(","))
    number_list = [int(i) for i in str_number_list]
    print(insertion_sort(number_list))
