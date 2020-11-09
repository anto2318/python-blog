def binarySearch(list, start, end, value):
    mid = (start +  end)//2
    if start > end:
        return -1
    elif value > list[mid]:
        return binarySearch(list, mid + 1, end, value)
    elif value < list[mid]:
        return binarySearch(list, start, mid - 1, value)
    else:
        return mid

size = int(input("Enter size of list: "))
my_list = []
my_list.extend(range(0, size))
value = int(input("Enter a value to search: "))

position = binarySearch(my_list, 0, size - 1, value)
if position > -1:
    print(f'{value} found at position {position+1}\n')
else:
    print(f'{value} not found\n')