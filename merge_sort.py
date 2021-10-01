"""
Pseudocode for Merge sort

merge_sort(A, p, r)
    if p < r
        q  = ⌊(p + r) / 2⌋
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
    merge(A, p, q, r)

merge(A, p, r)
    n₁ = q - p + 1
    n₂ = r - q
    create arrays L[1.. n₁+1] and R[1.. n₂+1]
    for i = 1 to n₁
        L[i] = A[p+i-1]
    for j = 1 to n₂
        R[j] = A[q+j]
    L[n₁ + 1] = ∞
    R[n₂ + 1] = ∞
    i = 1
    j = 1
    for k = p to r
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else A[k] = R[j]
            j = j + 1


* A - array name
* p - first index (not value in index just index number)
* r - last index  (not value in index just index number)
|
* Recursive Algorithm
* Division part is simple
* Combine part is complex
|
* Merge sort have best case only, because always partitions are balanced
    T(n) = 2T(n/2) + c₃n --> O(n log₂ n)  --> similar to quick sort best case
"""

import math
import sys


def merge_sort(a, p, r):
    """
    This algorithm use to sort number lists

    Args:
        a: Unsorted list of numbers
        p: first index of list (most of cases 0)
        r: last index of list

    Returns:
        Sorted list of numbers
    """

    q = math.floor((p + r) / 2)
    if p < r:
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
    _merge(a, q)

    return a


def _merge(a, q):
    left = a[:q]
    right = a[q:]

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    str_number_list = (sys.argv[1].split(","))
    number_list = [int(i) for i in str_number_list]
    first = 0
    last = len(number_list) - 1
    print(merge_sort(number_list, first, last))
