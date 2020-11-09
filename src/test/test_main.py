import sys
sys.path.insert(0, '/bin/interpolation_search.py')

from bin.interpolation_search import interpolationSearch

n = 10
my_list = []
my_list.extend(range(0, n))
x = 3
position = interpolationSearch(my_list, 0, n - 1, x)
if position > -1:
    print(f'{x} found at position {position+1}\n')
else:
    print(f'{x} not found\n')