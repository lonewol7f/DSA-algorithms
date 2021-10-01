"""
Pseudocode for heap_insert

heap_insert(A, key)
    A.heap_size = A.heap_size + 1
    i = A.heap_size (assume A[i] is -infinity)
    while i > 1 and A[parent(i)] < key
        A[i] = A[parent(i)]
        i = parent(i)

    A[i] = key

|
* A - array name
* key - value that wants to insert
|
* T(n) = O(log₂ n)
"""


def heap_insert(array, key):
    array.append(None)
    i = len(array) - 1
    parent = (len(array) // 2) - 1
    while i > 0 and array[parent] < key:
        array[i] = array[parent]
        i = parent
        parent = (i // 2) - 1

    array[i] = key
    return array


if __name__ == '__main__':
    number_list = [100, 80, 70, 10, 20]
    print(heap_insert(number_list, 200))
