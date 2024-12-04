import re

chars = set('0123456789,')
list_of_safe_inputs = []
total = 0

with open('input.txt', 'r') as file:
    input_text = file.read()

do_dont_safe_input = input_text.split('do')

for do_donts in do_dont_safe_input:
    if do_donts.startswith("n't()"):
        continue
    elif do_donts.startswith('()'):
        safe_input = re.findall(r'mul\((.*?)\)', do_donts)
        for unique_input in safe_input:
            safe_bool = True
            for letter in unique_input:
                if letter not in chars:
                    safe_bool = False
            if safe_bool:
                list_of_safe_inputs.append(unique_input)
            else:
                inner_mul_check = unique_input.split('mul(')
                inner_mul_bool = True
                for inner_muls in inner_mul_check:
                    for inner_mul_letter in inner_muls:
                        if inner_mul_letter not in chars:
                            inner_mul_bool = False
                    if inner_mul_bool:
                        print(inner_muls)
                        split_inner_muls = inner_muls.split(',')
                        total = total + (int(split_inner_muls[0]) * int(split_inner_muls[1]))
                    inner_mul_bool = True

for mults in list_of_safe_inputs:
    split_mults = mults.split(',')
    total = total + (int(split_mults[0]) * int(split_mults[1]))

print(total)
