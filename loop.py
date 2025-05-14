list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]


def print_positive_numbers(lst):
    positive_nums = [num for num in lst if num > 0] # List comprehension to add only positive numbers to a new list
    print("Output:", positive_nums)
    print()

# Input and Output for list1
print("Input: list1 =", list1)
print_positive_numbers(list1)

# Input and Output for list2
print("Input: list2 =", list2)
print_positive_numbers(list2)

