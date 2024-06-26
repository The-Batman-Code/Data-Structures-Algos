def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quicksort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quicksort_helper(my_list, left, pivot_index - 1)
        quicksort_helper(my_list, pivot_index + 1, right)
    return my_list


def quicksort(my_list):
    return quicksort_helper(my_list, 0, len(my_list) - 1)


# TC of the above quicksort algo functions combined is O(nlogn) on avg and O(n^2) in worst case. SC is O(nlogn) due to recursive calls

my_list = [3, 5, 0, 6, 2, 1, 4]
print(pivot(my_list, 0, 6))
print(quicksort(my_list))
