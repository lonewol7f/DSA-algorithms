"""
Pseudocode for build_heap

build_heap(A)
    A.heap_size = A.length
    for i = ⌊A.length / 2⌋ downto 1
        heapify(A, i)

heapify(A, i)
    l = left[i]
    r = right[i]

    if l <= A.heap_size and a[l] >A[i]
        largest = l
    else
        largest = i

    if r <= A.heap_size and a[r] >A[largest]
        largest = r

    if largest != i
        exchange A[i] with A[largest]
        heapify(A, largest)

* A - array name
|
* we can use this algorithm when we have more than one node violation
|
* T(n) = O(n)

"""


def build_heap(array):
    for i in range((len(array) // 2) - 1, -1, -1):
        _heapify(array, i)

    return array


def _heapify(array, index):
    left = 2 * index + 1
    right = 2 * index + 2

    if left < len(array) and array[left] > array[index]:
        largest = left
    else:
        largest = right

    if right < len(array) and array[right] > array[largest]:
        largest = right

    if largest != index and largest < len(array):
        array[index], array[largest] = array[largest], array[index]
        _heapify(array, largest)


if __name__ == '__main__':
    number_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(build_heap(number_list))
