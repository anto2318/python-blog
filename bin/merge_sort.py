def merge(list, left, mid, right):
    n1, n2 = mid - left + 1, right - mid

    L = [list[left + i] for i in range(n1)]
    R = [list[mid + 1 + j] for j in range(n2)]

    k = left
    while L and R:
        if L[0] <= R[0]:
            list[k] = L.pop(0)
        else:
            list[k] = R.pop(0)
        k += 1

    if L:
        list[k: k + len(L)] = L
        k += len(L)
    if R:
        list[k: k + len(R)] = R

    return list

def mergeSort(list, left, right):
    if left < right:
        mid = (left + (right - 1))//2
        mergeSort(list, left, mid)
        mergeSort(list, mid + 1, right)
        merge(list, left, mid, right)
    return list

my_list = [5, 9, 1, 4, 2, 8, 0, 3, 7, 6]
print("Original list: \n", my_list)

mergeList = mergeSort(my_list, 0, len(my_list) - 1)
print("\nSorted list: \n ", mergeList)

