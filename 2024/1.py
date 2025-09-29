list_1 = []
list_2 = []
distance_list = []

with open('input_file', 'r') as file:
        for line in file:
                current_line = line.split('   ')
                list_1.append(int(current_line[0]))
                list_2.append(int(current_line[1]))

list_1.sort()
list_2.sort()


index = 0

for number in list_1:
        distance_list.append(abs(list_1[index] - list_2[index]))
        index = index + 1

total_diff = 0

for diff in distance_list:
        total_diff = total_diff + diff

print(total_diff)

similarity_score = 0

for number_1 in list_1:
        current_similarity = 0
        for number_2 in list_2:
                if number_1 == number_2:
                        current_similarity = current_similarity + 1
        current_similarity = number_1 * current_similarity
        similarity_score = similarity_score + current_similarity

print(similarity_score)
