# https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

l = [3, 9, 4, 2, 1, 5]
insertion_sort(l)
print(l)
