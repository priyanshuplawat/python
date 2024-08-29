#1
dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
values =dict.values()
mean = sum(values)/len(values)
print(f"The mean of the values is: {mean:.1f}")

"""output is
The mean of the values is: 6.2"""

#2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print(result)

"""output is
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

#3
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
keys = dict1.keys()
values = dict1.values()
items = dict1.items()
print("\nKeys:")
for key in keys:
    print(key)

print("\nValues:")
for value in values:
    print(value)

print("\nItems:")
for item in items:
    print(item)

"""output is
Keys:
1
2
3
4
5
6

Values:
10
20
30
40
50
60

Items:
(1, 10)
(2, 20)
(3, 30)
(4, 40)
(5, 50)
(6, 60)
"""

#4
dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
keys = dict.keys()
values =dict.values()
items =dict.items()

print("\nKeys:")
for key in keys:
    if key == 3:
      continue
    if key == 5:    
      continue
    print(key)

print("\nValues:")
for value in values:
    if value == None:
        continue
    if value == None:
        continue
    print(value)

print(" Dictionary with empty items dropped:")
filtered_dict = {key: value for key, value in dict.items() if value is not None}
print(filtered_dict)

"""output is
Keys:
1
2
4
6

Values:
10
20
40
60
 Dictionary with empty items dropped:
{1: 10, 2: 20, 4: 40, 6: 60}"""




