"""
Pseudocode for Quick sort

quick_sort(A,p,r)
    if p < r
        q = partition(A,p,r)  # same as divide
        quick_sort(A,p,q)
        quick_sort(A,q+1,r)

partition(A,p,r)    # method 2(pivot = p)
    x = A[p]
    i = p - 1
    j = r + 1
    while TRUE
        do repeat j = j - 1
                until A[j] <= x
            repeat i = i +1
                until A[i] >= x
            if i < j
                then exchange A[i] with A[j]
                else return j


* A - array name
* p - first index (not value in index just index number)
* r - last index  (not value in index just index number)
|
* Recursive Algorithm
* Division part (partition)  is complex
* Combine part is easy
|
* best case - when the partition is balanced (pivot is in the middle)
    T(n) = 2T(n/2) + c₂n --> O(n log₂ n)
* worst case - when partition is unbalanced (pivot is in one of the ends), T(n) goes high
    T(n) = T(n - 1) + c₂n --> c₂ * (n/2 + n²/2) --> O(n²)  --> Similar to insertion sort worst case

|
* Run in Terminal: `python3 quick_sort_2.py <number list seperated by comma without spaces>`
* Example: `python3 insertion_sort.py 12,4,25,28,5`

"""


import sys


def quick_sort(a, p, r):
    """
    This algorithm use to sort number lists

    Args:
        a: Unsorted list of numbers
        p: first index of list (most of cases 0)
        r: last index of list

    Returns:
        Sorted list of numbers

    """
    if p < r:
        q = _partition(a, p, r)
        quick_sort(a, p, q)
        quick_sort(a, q + 1, r)

    return a


def _partition(a, p, r):
    """
    Helper method for quick_sort()
    pivot = last element in list

    Args:
        a: Unsorted list of numbers
        p: first index of list (most of cases 0)
        r: last index of list

    Returns:
        pivot number's index

    """

    x = a[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j = j - 1
            if a[j] <= x:
                break
        while True:
            i = i + 1
            if a[i] >= x:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            return j


if __name__ == '__main__':
    str_number_list = (sys.argv[1].split(","))
    number_list = [int(i) for i in str_number_list]
    first = 0
    last = len(number_list) - 1
    print(quick_sort(number_list, first, last))
