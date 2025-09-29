def is_level_safe(level_list):
        list_len = len(level_list) - 1
        is_safe = True
        current_step = 0
        if level_list == sorted(level_list) or level_list == sorted(level_list, reverse=True):
                pass
        else:
                is_safe = False
                return is_safe
        while current_step < list_len:
                if abs(level_list[current_step] - level_list[current_step + 1]) == 0:
                        is_safe = False
                        break
                if abs(level_list[current_step] - level_list[current_step + 1]) > 3:
                        is_safe = False
                        break
                current_step += 1
        return is_safe

safe_counter = 0

def is_level_safe_with_dampener(level_list):
        if is_level_safe(level_list):
                return True
        is_safe = False
        for index,number in enumerate(level_list):
                temp_list = level_list[:]
                temp_list.pop(index)
                if is_level_safe(temp_list):
                        is_safe = True
                        break
        return is_safe

with open('input_file', 'r') as file:
        for line in file:
                current_level = [ int(x) for x in line.split() ]
                if is_level_safe(current_level):
                        safe_counter = safe_counter + 1

print(safe_counter)

new_safe_counter = 0 

with open('input_file', 'r') as file:
        for line in file:
                current_level = [ int(x) for x in line.split() ]
                if is_level_safe_with_dampener(current_level):
                        new_safe_counter = new_safe_counter + 1

print(new_safe_counter)
 
