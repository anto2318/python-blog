import heapq as H

def minHeap(list):
    H.heapify(list)
    return list

def heapPush(list, n):
    H.heappush(list, n)
    return list

def heapPop(list):
    H.heappop(list)
    return list

def heapPushPop(list, n):
    H.heappushpop(list, n)
    return list

list = [5, 1, 4, 2, 3]
print('Normal list: ',list)

list = minHeap(list)
print('Min heap: ', list)

list = heapPush(list, 9)
list = heapPush(list, 0)
print('Heap after push (9 & 0): ',list)

list = heapPop(list)
list = heapPop(list)
print('Heap after pop(0 & 1): ', list)

list = heapPushPop(list, 7)
print('Heap after pushpop(7,2): ',list)