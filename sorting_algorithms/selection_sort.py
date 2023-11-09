def selection_sort(nums: list) -> list:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    :param collection: A list of integers to be sorted.
    :return: The sorted list.

    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """


    length = len(nums)
    for i in range(length):
        current_min_index = i
        for j in range(i+1,length):
            if nums[j] < nums[current_min_index]: # here the operator can be changed to get from an ascending list to an decending list
                current_min_index = j
        if current_min_index != i:
            nums[i], nums[current_min_index] = nums[current_min_index], nums[i]

    return nums


print(selection_sort([1,5,3,8,1,2,3201,6]))


# if __name__ == '__main__':
#     user_input =  input('give me ur list that needs to be sorted (numbers separated by ","): ').strip()
#     input_list = [int(i) for i in user_input.split(',')]
#     sorted_list = selection_sort(input_list)
#     print(f'The sorted list is: {sorted_list}')

