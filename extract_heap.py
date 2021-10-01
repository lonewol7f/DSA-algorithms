"""
Pseudocode for extract_heap

extract_heap(A)
    if A.heap_size >= 1
        max = A[1]
        A[1] = A[A.heap_size]
        A.heap_size = A.heap_size - 1
        heapify(A, 1)
        return max

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

|
* T(n) = O(log₂ n)
"""


def extract_heap(array):
    if len(array) >= 1:
        max_num = array[0]
        array[0] = array[-1]
        del array[-1]
        _heapify(array, 0)

        return max_num


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
    number_list = [100, 80, 70, 10, 20]
    print(extract_heap(number_list))
