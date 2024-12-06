
from functools import cmp_to_key

input_data = []
rules_data_dict = {}

with open('input.txt', 'r') as f:
    for line in f:
        input_data.append(line.strip().split(','))

with open('rules.txt', 'r') as f:
    for line in f:
        temp_list = line.strip().split('|')
        if rules_data_dict.get(temp_list[0]):
            rules_data_dict[temp_list[0]].append(temp_list[1])
        else:
            rules_data_dict[temp_list[0]] = [temp_list[1]]


            
def assignment_one(input_assignment_one):
    sum_of_middle = 0
    for input_list in input_assignment_one:
        matching_bool = True
        sorted_input_list = sort_list_according_to_rules_bubble_sort(input_list[:], rules_data_dict)
        for n in range(len(input_list)):
            if input_list[n] != sorted_input_list[n]:
                matching_bool = False
        if matching_bool:
            n = int(len(input_list))
            sum_of_middle = sum_of_middle + int(input_list[int(((n-1)/2))])
    return sum_of_middle


def assignment_two(input_assignment_two):
    total = 0
    for input_list in input_assignment_two:
        ordered_list = reorder_update(input_list[:], rules_data_dict)
        if ordered_list != input_list:
            n = len(ordered_list)
            print(n)
            total = total + int(ordered_list[int((n-1)/2)])
    return total

def sort_list_according_to_rules_bubble_sort(unsorted_list, rules): #bubble sort, funkar inte för del två
    n = len(unsorted_list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if rules.get(unsorted_list[j+1]):
                if unsorted_list[j] in rules.get(unsorted_list[j+1]):
                    unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
        if not swapped:
            break
    sorted_list = unsorted_list
    return sorted_list

def rule_based_comparator(x, y, rules):
    if y in rules.get(x, set()):
        return -1
    if x in rules.get(y, set()):
        return 1
    return 0

def reorder_update(input_data, rules):
    return sorted(input_data, key=cmp_to_key(lambda a, b: rule_based_comparator(a, b, rules)))


                    
print(assignment_two(input_data)) 



#print(assignment_one(input_data))
#print(assignment_two(input_data))
