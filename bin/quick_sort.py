def partition(list, left, right):
    i = left - 1
    pivot = list[right]
    for j in range(left, right):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[right] = list[right], list[i + 1]
    return (i + 1)

def quickSort(list, left, right):
    if left < right:
        part = partition(list, left, right)
        quickSort(list, left, part - 1)
        quickSort(list, part + 1, right)
    return list

my_list = [5, 9, 1, 4, 2, 8, 0, 3, 7, 6]
print("Original list: \n", my_list)

quickList = quickSort(my_list, 0, len(my_list) - 1)
print("List with quick sort: \n", quickList)
