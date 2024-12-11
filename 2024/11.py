import re

input_data = '70949 6183 4 3825336 613971 0 15 182'
storage_dict = {}



def transform_stone(stone):
    #print(stone)
    if storage_dict.get(stone):
        #print(stone)
        return storage_dict.get(stone)
    else:
        if stone == '0':
            # Rule 1: Replace 0 with 1
            storage_dict[stone] = ['1']
            return ['1']
        elif len(stone) % 2 == 0:
            # Rule 2: Split evenly if the number of digits is even
            mid = len(stone) // 2
            left = stone[:mid].lstrip('0') or '0'
            right = stone[mid:].lstrip('0') or '0'
            storage_dict[stone] = [left, right]
            return [left, right]
        else:
            # Rule 3: Multiply by 2024 otherwise
            storage_dict[stone] = [str(int(stone) * 2024)]
            return [str(int(stone) * 2024)]


def blinks(stones, current_blinks=0):
    current_blinks += 1
    print(current_blinks)
    if current_blinks > blink_counter:
        # Return the count of stones directly
        return len(stones)
    else:
        # Create a new list to hold transformed stones
        new_stones = []
        for stone in stones:
            new_stones.extend(transform_stone(stone))
        
        # Recurse with the new list of stones
        return blinks(tuple(new_stones), current_blinks)

blink_counter = 75

# Convert the input into a list of stones
stones = tuple(input_data.split())
counted_stones = blinks(stones, 0)

print(counted_stones)
