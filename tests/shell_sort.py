# https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

        gap = gap//2

l = [3, 9, 4, 2, 1, 5]
shellSort(l)
print(l)
