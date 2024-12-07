from itertools import product
from datetime import datetime
startTime = datetime.now()
input_data = []

with open('input.txt', 'r') as f:
    for line in f:
        temp_string = line.strip()
        temp_string = temp_string.replace(':','')
        temp_string = temp_string.replace(' ', ', ')
        temp_string = '(' + temp_string + ')'
        res_tup = eval(temp_string)
        input_data.append(res_tup)


def remove_invalid_equations(list_of_equations):
    valid_equations = []
    
    for equation in list_of_equations:
        target_value = equation[0]  
        numbers = equation[1:]  
        
        n = len(numbers)
        
        for ops in product(['+', '*', '||'], repeat=n-1):
            result = int(numbers[0])
            
            for i, op in enumerate(ops):
                if op == '+':
                    result += int(numbers[i+1])
                elif op == '*':
                    result *= int(numbers[i+1])
                elif op == '||':
                    result = int(str(result) + str(numbers[i+1]))
                
            if result == target_value:
                valid_equations.append((target_value))
                break
    return valid_equations

def part_one_and_two(input_parts):
    total = 0
    equations = remove_invalid_equations(input_parts)
    for equation in equations:
        total = total + int(equation)
    print(total)


part_one_and_two(input_data)
print(datetime.now() - startTime)
