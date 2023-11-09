def merge_sort_recursive(nums: list) -> list:
    def merge(left: list, right: list) -> list:
        """
        Merge two sorted lists into a single sorted list.

        :param left: Left collection
        :param right: Right collection
        :return: Merged result
        """
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(nums) <= 1:
        return nums
    mid_index = len(nums) // 2
    return merge(merge_sort_recursive(nums[:mid_index]), merge_sort_recursive(nums[mid_index:]))



def merge(input_list: list, low: int, mid: int, high: int) -> list:
    """
    sorting left-half and right-half individually
    then merging them into result
    """
    result = []
    left, right = input_list[low:mid], input_list[mid : high + 1]
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    input_list[low : high + 1] = result + left + right
    return input_list


def merge_sort_iterative(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    nums = list(nums)

    # iteration for two-way merging
    p = 2
    while p <= len(nums):
        # getting low, high and middle value for merge-sort of single list
        for i in range(0, len(nums), p):
            low = i
            high = i + p - 1
            mid = (low + high + 1) // 2
            nums = merge(nums, low, mid, high)
        # final merge of last two parts
        if p * 2 >= len(nums):
            mid = i
            nums = merge(nums, 0, mid, len(nums) - 1)
            break
        p *= 2

    return nums





if __name__ == "__main__":
    import doctest
    from random import sample
    from timeit import timeit

    doctest.testmod()

    # Benchmark: Iterative seems slightly faster than recursive.
    num_runs = 10_000
    unsorted = sample(range(-50, 50), 100)
    timer_iterative = timeit(
        "merge_sort_iterative(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nIterative merge sort:")
    print(*merge_sort_iterative(unsorted), sep=",")
    print(f"Processing time (merge iterative): {timer_iterative:.5f}s for {num_runs:,} runs")

    unsorted = sample(range(-50, 50), 100)
    timer_recursive = timeit(
        "merge_sort_recursive(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\Recursive merge sort:")
    print(*merge_sort_recursive(unsorted), sep=",")
    print(f"Processing time (merge recursive): {timer_recursive:.5f}s for {num_runs:,} runs")



# Iterative merge sort:
# -50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
# Processing time (merge iterative): 1.32581s for 10,000 runs
# \Recursive merge sort:
# -50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
# Processing time (merge recursive): 1.48659s for 10,000 runs