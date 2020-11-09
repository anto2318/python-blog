def selectionSort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

my_list = [5, 9, 1, 4, 2, 8, 0, 3, 7, 6]
print("Original list: \n", my_list)
print("\nSorted list: \n ",selectionSort(my_list))