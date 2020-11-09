def insertionSort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while temp < list[j] and j >= 0:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list

my_list = [5, 9, 1, 4, 2, 8, 0, 3, 7, 6]
print("Original list: \n", my_list)

print("List with insertion sort: \n", insertionSort(my_list))