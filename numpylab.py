#1
import numpy as np

my_list = [1, 2, 3, 4, 5]
array_list = np.array(my_list)
print("numpy array:",array_list)

"""output is
numpy array: [1 2 3 4 5]"""

#2
my_list2 = [1, 2, 3, 4, 5]
array_list2 = np.array(my_list2)
print("numpy array:",array_list2)
print("First element:",array_list2[0])
print("Last element:",array_list2[4])
print(array_list*2)

"""output is
numpy array: [1 2 3 4 5]
First element: 1
Last element: 5
[ 2  4  6  8 10]"""



