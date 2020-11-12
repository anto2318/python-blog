import heapq as H

negativeList = lambda x:list(map(lambda y:-y, x))

def maxHeap(my_list):
    H.heapify(my_list)
    return my_list

def heapPush(my_list, n):
    H.heappush(my_list, n)
    return my_list

def heapPop(my_list):
    H.heappop(my_list)
    return my_list

my_list = [1, 5, 8, 2, 3]
print('Normal my_list: ',my_list)

my_list = negativeList(my_list)
print('Negative list: ',my_list)

my_list = maxHeap(my_list)
print('Max heap: ', negativeList(my_list))

my_list = heapPush(my_list, -4)
print('Heap after push 4: ', negativeList(my_list))

data = heapPop(my_list)
print('Heap after pop: ', negativeList(my_list))