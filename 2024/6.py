from copy import deepcopy

with open('input.txt', 'r') as f:
    input_data = [[str(num) for num in line.strip()] for line in f]

x_len = len(input_data)
y_len = len(input_data[0])
map_for_part_two = deepcopy(input_data)

def get_start_pos():
    start_strings = '<>^v'
    for x in range(x_len):
       for y in range(y_len):
          if input_data[x][y] in start_strings:
            start_x_pos = x
            start_y_pos = y
    return start_x_pos, start_y_pos

start_x_pos, start_y_pos = get_start_pos()

class guard():
   current_x_pos = start_x_pos #lodrätt
   current_y_pos = start_y_pos #vågrätt
   current_direction = 'upwards' #input_data[current_x_pos][current_y_pos]
   inbound = True
   not_looped = True
   last_visited_x_chord = 0
   last_visited_y_chord = 0

the_guard = guard

x_path_cords = []
y_path_cords = []

def part_one():
    while the_guard.inbound:
        if the_guard.current_direction == 'upwards':
            if the_guard.current_x_pos - 1 < 0:
                input_data[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                the_guard.inbound = False
            elif input_data[the_guard.current_x_pos - 1][the_guard.current_y_pos] == '#':
                the_guard.current_direction = 'right'
            else:
                input_data[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                x_path_cords.append(the_guard.current_x_pos)
                y_path_cords.append(the_guard.current_y_pos)
                the_guard.current_x_pos = the_guard.current_x_pos - 1
        if the_guard.current_direction == 'downwards':
            if the_guard.current_x_pos + 1 == x_len:
                input_data[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                the_guard.inbound = False
            elif input_data[the_guard.current_x_pos + 1][the_guard.current_y_pos] == '#':
                the_guard.current_direction = 'left'
            else:
                input_data[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                x_path_cords.append(the_guard.current_x_pos)
                y_path_cords.append(the_guard.current_y_pos)
                the_guard.current_x_pos = the_guard.current_x_pos + 1
        if the_guard.current_direction == 'left':
            if the_guard.current_y_pos - 1 < 0:
                input_data[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                the_guard.inbound = False
            elif input_data[the_guard.current_x_pos][the_guard.current_y_pos - 1] == '#':
                the_guard.current_direction = 'upwards'
            else:
                input_data[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                x_path_cords.append(the_guard.current_x_pos)
                y_path_cords.append(the_guard.current_y_pos)
                the_guard.current_y_pos = the_guard.current_y_pos - 1
        if the_guard.current_direction == 'right':
            if the_guard.current_y_pos + 1 == y_len:
                input_data[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                the_guard.inbound = False
            elif input_data[the_guard.current_x_pos][the_guard.current_y_pos + 1] == '#':
                the_guard.current_direction = 'downwards'
            else:
                input_data[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                x_path_cords.append(the_guard.current_x_pos)
                y_path_cords.append(the_guard.current_y_pos)
                the_guard.current_y_pos = the_guard.current_y_pos + 1

    return None

def count_steps():
    x_count = 0
    for x in range(x_len):
       for y in range(y_len):
          if input_data[x][y] == 'X':
             x_count = x_count + 1
    return x_count

part_one()


def part_two():
    block_x_chords = []
    block_y_chords = []
    for step in range(len(x_path_cords)):
        the_guard.current_x_pos = start_x_pos
        the_guard.current_y_pos = start_y_pos
        the_guard.current_direction = 'upwards'
        the_guard.inbound = True
        the_guard.not_looped = True
        map_copy = deepcopy(map_for_part_two)
        map_copy[x_path_cords[step]][y_path_cords[step]] = '#'
        map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
        buffer = []
        buffer_size = 500
        while the_guard.inbound and the_guard.not_looped:
            buffer.append(map_copy[the_guard.current_x_pos][the_guard.current_y_pos])
            while len(buffer) > buffer_size:
                buffer.pop(0)
            if the_guard.current_direction == 'upwards':
                if the_guard.current_x_pos - 1 < 0:
                    map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                    the_guard.inbound = False
                elif map_copy[the_guard.current_x_pos - 1][the_guard.current_y_pos] == '#':
                    the_guard.current_direction = 'right'
                else:
                    map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                    the_guard.current_x_pos = the_guard.current_x_pos - 1
            if the_guard.current_direction == 'downwards':
                if the_guard.current_x_pos + 1 >= x_len:
                    #print('out')
                    map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                    the_guard.inbound = False
                elif map_copy[the_guard.current_x_pos + 1][the_guard.current_y_pos] == '#':
                    the_guard.current_direction = 'left'
                else:
                    map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                    the_guard.current_x_pos = the_guard.current_x_pos + 1
            if the_guard.current_direction == 'left':
                if the_guard.current_y_pos - 1 < 0:
                    map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                    the_guard.inbound = False
                elif map_copy[the_guard.current_x_pos][the_guard.current_y_pos - 1] == '#':
                    the_guard.current_direction = 'upwards'
                else:
                    map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                    the_guard.current_y_pos = the_guard.current_y_pos - 1
            if the_guard.current_direction == 'right':
                if the_guard.current_y_pos + 1 == y_len:
                    map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                    the_guard.inbound = False
                elif map_copy[the_guard.current_x_pos][the_guard.current_y_pos + 1] == '#':
                    the_guard.current_direction = 'downwards'
                else:
                    map_copy[the_guard.current_x_pos][the_guard.current_y_pos] = 'X'
                    the_guard.current_y_pos = the_guard.current_y_pos + 1
            if len(buffer) >= buffer_size:
                if all(item == 'X' for item in buffer):
                    the_guard.not_looped = False

            if not the_guard.not_looped:
                block_x_chords.append(x_path_cords[step])
                block_y_chords.append(y_path_cords[step])
                break
              
    pos_set = set()
    for x in range(len(block_x_chords)):
        pos_set.add(str(str(block_x_chords[x]) + '-' + str(block_y_chords[x])))
    print(len(pos_set))
                

part_two()
