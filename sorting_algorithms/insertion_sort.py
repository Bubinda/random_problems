def insertion_sort_1(nums: list) -> list:
    """
    Insertion sort algorithm
    """
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums



def insertion_sort_2(nums: list) -> list:
    
    for i in range(1,len(nums)):
        curr_value = nums[i]
        while i > 0 and curr_value < nums[i-1]:
            nums[i] = nums[i-1]
            i -= 1
        nums[i] = curr_value
    return nums


if __name__ == "__main__":
    import doctest
    from random import sample
    from timeit import timeit

    doctest.testmod()

    # Benchmark: Iterative seems slightly faster than recursive.
    num_runs = 10_000
    unsorted = sample(range(-50, 50), 100)
    timer_iterative_1 = timeit(
        "insertion_sort_1(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nIterative insertnion sort 1:")
    print(*insertion_sort_1(unsorted), sep=",")
    print(f"Processing time (1): {timer_iterative_1:.5f}s for {num_runs:,} runs")

    unsorted = sample(range(-50, 50), 100)
    timer_iterative_2 = timeit(
        "insertion_sort_2(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nIterative insertion sort 2:")
    print(*insertion_sort_2(unsorted), sep=",")
    print(f"Processing time (2): {timer_iterative_2:.5f}s for {num_runs:,} runs")




# Iterative insertion sort 1:
# -50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
# Processing time (1): 4.22693s for 10,000 runs

# Iterative insertion sort 2:
# -50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
# Processing time (2): 3.04746s for 10,000 runs