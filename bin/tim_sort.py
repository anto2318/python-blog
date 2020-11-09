run = 4

def selectionSort(list, start, end):
    for i in range(start, end):
        min = i 
        for j in range(i, end):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

def merge(list, pos, mid, end):
    n1, n2 = mid - pos + 1, end - mid
    L = [list[pos + i] for i in range(n1)]
    R = [list[mid + 1 + j] for j in range(n2)]
    k = pos

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

def timSort(list):
    totalLen = len(list)
    for i in range(0, totalLen, run):
        j = min(i + run, totalLen)
        list = selectionSort(list, i, j)

    size = run
    while size < totalLen:
        for i in range(0, totalLen, size * 2):
            mid = min(totalLen - 1, i + size - 1)
            end = min(totalLen - 1, mid + size)
            list = merge(list, i, mid, end)
        size *= 2
    return list

my_list = [5, 9, 1, 4, 2, 8, 0, 3, 7, 6]
print("Original list: \n", my_list)
print("\nSorted list: \n ",timSort(my_list))