
def interpolationSearch(list, low, high, value):
    if(low <= high and value >= list[low] and value <= list[high]):
        position = low + ((high - low) // (list[high] - list[low]) * (value - list[low]))
        if list[position] == value:
            return position
        if list[position] < value:
            return interpolationSearch(list, position + 1, high, value)
        if list[position] > value:
            return interpolationSearch(list, low, position - 1, value)
        return -1


size = int(input("Enter size of list: "))
my_list = []
my_list.extend(range(0, size))
value = int(input("Enter a value to search: "))
position = interpolationSearch(my_list, 0, size - 1, value)
if position > -1:
    print(f'{value} found at position {position+1}\n')
else:
    print(f'{value} not found\n')