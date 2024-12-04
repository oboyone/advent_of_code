safe_counter = 0
safe_dampened_counter = 0
list_of_lists = []
lines = 0

with open('input.txt', 'r') as file:
    for line in file:
        list_of_lists.append(line.strip().split(' '))

for inner_list in list_of_lists:
    safe_bool = True
    increasing_bool = True
    decreasing_bool = True
    for x in range(len(inner_list)):
        if x == 0:
            previous_number = int(inner_list[x])
            continue
        if abs(int(inner_list[x]) - int(previous_number)) > 3:
            safe_bool = False
            break
        if int(inner_list[x]) > int(previous_number):
            decreasing_bool = False
        if int(inner_list[x]) < int(previous_number):
            increasing_bool = False
        if int(inner_list[x]) == int(previous_number):
            safe_bool = False
            break
        previous_number = inner_list[x]
        if decreasing_bool == False and increasing_bool == False:
            safe_bool = False
            break
    if safe_bool == True:
        safe_counter = safe_counter + 1
    if safe_bool == False:
        for y in range(len(inner_list)):
            sliced_list = inner_list[:]
            sliced_list.pop(y)
            history_list = []
            safe_bool = True
            for x in range(len(sliced_list)):
                if x == 0:
                    previous_number = int(sliced_list[x])
                    continue
                if abs(int(sliced_list[x]) - int(previous_number)) > 3:
                    safe_bool = False
                    continue
                if int(sliced_list[x]) > int(previous_number):
                    history_list.append('d')
                if int(sliced_list[x]) < int(previous_number):
                    history_list.append('i')
                if int(sliced_list[x]) == int(previous_number):
                    safe_bool = False
                if 'd' in history_list and 'i' in history_list:
                    safe_bool = False
                previous_number = sliced_list[x]
            if safe_bool == True:
                safe_counter = safe_counter + 1
                break
            else:
                print(inner_list)
                print(sliced_list)



print(safe_counter)
        
            
        
