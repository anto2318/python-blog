from heapq import *

def heapSort(list, size):
    heap = []

    for i in list:
        heappush(heap, i)

    return [heappop(heap) for i in range(size)]

my_list = [5, 9, 1, 4, 2, 8, 0, 3, 7, 6]
print("Original list: \n", my_list)

heapList = heapSort(my_list, len(my_list))
print("List with heap sort: \n", heapList)