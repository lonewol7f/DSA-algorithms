"""
Pseudocode for heap_sort

heap_sort(A)
    build_heap(A)
    for i = A.length downto 2
        exchange A[1] with A[i]
        A.heap_size = A.heap_size - 1
        heapify(A, 1)

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

|
Running Time:
    step 1 (build_heap) - O(n)
    step 2 to 5 (heapify O(log₂ n) and there are (n - 1) calls)
    overall - O(n log₂ n)

"""


def heap_sort(array):
    sorted_array = []
    _build_heap(array)
    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        sorted_array.insert(0, array[-1])
        del array[-1]
        _heapify(array, 0)

    return sorted_array


def _build_heap(array):
    for i in range((len(array) // 2) - 1, -1, -1):
        _heapify(array, i)


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
    number_list = [4, 8, 7, 110, 20, 15, 43]
    print(heap_sort(number_list))
