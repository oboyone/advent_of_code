import numpy as np

with open('input.txt', 'r') as f:
    input_data = [[str(num) for num in line.strip()] for line in f]

def search_for_string(input_matrix, search_string):
    counter = 0
    #search_list = [str(a) for a in search_string]
    for row in input_matrix:
        counter = counter + int(''.join(row).count(search_string))
        reverse_row = row[::-1]
        counter = counter + int(''.join(reverse_row).count(search_string))
    return int(counter)


max_col = len(input_data[0])
max_row = len(input_data)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(input_data[y][x])
        rows[y].append(input_data[y][x])
        fdiag[x+y].append(input_data[y][x])
        bdiag[x-y-min_bdiag].append(input_data[y][x])



counter = search_for_string(cols, 'XMAS') + search_for_string(rows, 'XMAS') + search_for_string(bdiag, 'XMAS') + search_for_string(fdiag, 'XMAS')

print(counter)

def find_mas_in_matrix():
    mas_count = 0
    for r in range(len(input_data)):
        for c in range(len(input_data[0])):
            if r != 0 and r != len(input_data)-1 and c != 0 and c != len(input_data[0])-1:
                if input_data[r][c] == 'A':
                    string_var = input_data[r-1][c-1] + input_data[r-1][c+1] + input_data[r+1][c-1] + input_data[r+1][c+1]
                    m_count = string_var.count('M')
                    s_count = string_var.count('S')
                    if m_count == 2 and s_count == 2 and input_data[r-1][c-1] != input_data[r+1][c+1] and input_data[r-1][c+1] != input_data[r+1][c-1]:
                        mas_count = mas_count + 1
                

    return mas_count
    
mas_counter = find_mas_in_matrix()

print(mas_counter)
