#1
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = set1.union(set2)
print("Unique items from set1 and set2:", unique_items)

"""output is
Unique items from set1 and set2: {70, 40, 10, 50, 20, 60, 30}"""

#2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.symmetric_difference(set2)

print("Elements present in Set A or B, but not both:", set3)

"""output is
Elements present in Set A or B, but not both: {20, 70, 10, 60}"""

#3
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
common_elements = set1 & set2
print("the common element is:",common_elements)

"""output is
the common element is:{10}"""

#4
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
common_elements = set1.intersection(set2)
set1.intersection_update(set2)
print("output after remove uncommon element:", set1)

"""output is
output after remove uncommon element: {40, 50, 30}"""


