#1
list1 = ["hello"]
list2 = ["world"]
list3 = list1+list2
print(sum)

"""output is
['hello', 'world']"""

#2
list = ['red', 'green', 'white', 'black']
print("Original list:", list)
print("Traverse the original list in reverse order:")
for index in range(len(list) - 1, -1, -1):
    print(list[index])

"""output is
Original list: ['red', 'green', 'white', 'black']
Traverse the original list in reverse order:
black
white
green
red"""

#3
def largest_smalest(numbers):
    if not numbers:
        return None, None
    largest = smallest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    return largest, smallest
numbers = [34, -2, 45, 0, 99, -56, 23]
largest, smallest = largest_smalest(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)

"""output is
Largest number: 99
Smallest number: -56"""

#4

def find_duplicates(numbers):
    count_dict = {}
    duplicates = set()

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count > 1:
            duplicates.add(num)
    
    return duplicates

numbers = [1, 3, 5, 3, 7, 9, 1, 5, 11]
duplicates = find_duplicates(numbers)
print("Duplicate values:", duplicates)


"""output is
Duplicate values: {1, 3, 5}"""

#5

def split_list(original_list, length_of_first_part):
    original list
    if length_of_first_part > len(original_list):
        raise ValueError("Length of the first part cannot be greater than the length of the original list.")
    
    first_part = original_list[:length_of_first_part]
    second_part = original_list[length_of_first_part:]
    
    return first_part, second_part

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3
first_part, second_part = split_list(original_list, length_of_first_part)

print("Original list:", original_list)
print("Length of the first part of the list:", length_of_first_part)
print("Splitted the said list into two parts:", (first_part, second_part))


"""output is
Original list: [1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])"""

