import heapq as H

list = [5, 1, 4, 2, 3]
print("Normal list: ", list)

H.heapify(list)
print("Min Heap: ",list)

H.heappush(list, 9)
H.heappush(list, 0)
print("Heap after push(9 & 0): ", list)

H.heappop(list)
H.heappop(list)

print("Heap after pop(0 & 1)")
H.heappushpop(list, 7)

print("Heap after pushpop(7, 2)", list)