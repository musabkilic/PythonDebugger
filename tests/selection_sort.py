# https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

l = [3, 9, 4, 2, 1, 5]
selection_sort(l)
print(l)
