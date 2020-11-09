def linearSearch(list, size, value):
    for i in range(size):
        if list[i] == value:
            return i
    return -1

size = int(input("Enter size of list: "))
my_list = []
my_list.extend(range(0, size))
value = int(input("Enter a value to search: "))
position = linearSearch(my_list, size, value)
if position > -1:
    print(f'{value} found at position {position+1}\n')
else:
    print(f'{value} not found\n')
