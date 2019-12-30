# https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
def bubble_sort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

l = [3, 9, 4, 2, 1, 5]
bubble_sort(l)
print(l)
