"""
Pseudocode for heapify

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
* i - index of violating node
|
* we can use this algorithm when we have only one node violation
|
* T(n) = O(log₂ n) --> O(h)
    since heapify applied for complete binary tree; \n
    *h = ⌊log₂ n⌋* Therefore, we can omit floor value because of that in Big O notation
    we talk about upper limit, Therefore no need to think about floor value

"""


def heapify(array, index):
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
        heapify(array, largest)

    return array


if __name__ == '__main__':

    num_list = [7, 24, 19, 21, 14, 3, 10, 2, 13, 11]

    print(heapify(num_list, 0))
