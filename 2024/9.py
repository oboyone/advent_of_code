from copy import deepcopy

with open('input.txt', 'r') as file:
    input_data = file.readline()


class data_block:
    block_id = int()
    #block_size = int()






def fill_data_list():
    data_block_or_free_space_counter = 0
    id_counter = 0
    data_list = []
    for input_number in input_data:
        if data_block_or_free_space_counter == 0 or data_block_or_free_space_counter % 2 == 0:
            temp_data_block = data_block()
            temp_data_block.block_id = id_counter
            #temp_data_block.block_size = input_number
            for x in range(0, int(input_number)):
                data_list.append(temp_data_block)
            id_counter += 1
        else:
            for x in range(0, int(input_number)):
                data_list.append('.')
        data_block_or_free_space_counter += 1
    return data_list

def sort_data_list(data_list):
    return_copy = deepcopy(data_list)
    data_list_copy = deepcopy(data_list)
    moved_elements = []
    for x in range(0, len(return_copy)):
        if return_copy[x] == '.':
            data_list_copy_len = len(data_list_copy) - 1
            for y in range(data_list_copy_len, 0, -1):
                if data_list_copy[y] != '.':

                    return_copy[x] = data_list_copy[y]
                    moved_elements.insert(0, data_list_copy.pop(y))
                else:
                    data_list_copy.pop(y)
    total_moved = len(moved_elements)
    print(total_moved)
    print(len(return_copy))
    for x in range(len(return_copy)-1, 0, -1):
        if total_moved == 0:
            print('asd')
            break
        elif return_copy[x] == '.':
            continue
        else:
            return_copy[x] = '.'
            total_moved -= 1
            #print(x)
    return return_copy


            

resulting_list = sort_data_list(fill_data_list())

for value in resulting_list:
    if value != '.':
        print(value.block_id)
    #else:
     #   print(value)
#print(resulting_list)
    
