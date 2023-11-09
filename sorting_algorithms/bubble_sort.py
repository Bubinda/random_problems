def bubble_sort(nums: list) -> list:
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1], nums[j]
    return nums




# alternate implemntation:

def bubble_sort_2(nums: list) -> list:
    length = len(nums)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                swapped = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return nums



# recursive implementation
def bubble_sort_recursive(nums: list) -> list:
    nums_length = len(nums)
    swapped = False

    for i in range(nums_length-1):
        if nums[i] > nums[i+1]:
            nums[i] , nums[i+1] = nums[i+1], nums[i]
            swapped = True
    
    return nums if not swapped else bubble_sort_recursive(nums)



if __name__ == "__main__":
    import doctest
    from random import sample
    from timeit import timeit

    doctest.testmod()

    # Benchmark: Iterative seems slightly faster than recursive.
    num_runs = 10_000
    unsorted = sample(range(-50, 50), 100)
    timer_iterative_1 = timeit(
        "bubble_sort(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nIterative bubble sort:")
    print(*bubble_sort(unsorted), sep=",")
    print(f"Processing time (iterative_1): {timer_iterative_1:.5f}s for {num_runs:,} runs")

    unsorted = sample(range(-50, 50), 100)
    timer_iterative_2 = timeit(
        "bubble_sort_2(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nIterative bubble sort:")
    print(*bubble_sort_2(unsorted), sep=",")
    print(f"Processing time (iterative_2): {timer_iterative_2:.5f}s for {num_runs:,} runs")


    unsorted = sample(range(-50, 50), 100)
    timer_recursive = timeit(
        "bubble_sort_recursive(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nRecursive bubble sort:")
    print(*bubble_sort_recursive(unsorted), sep=",")
    print(f"Processing time (recursive): {timer_recursive:.5f}s for {num_runs:,} runs")



# Iterative bubble sort 1:
# -50,-49,-48,-47,-45,-41,-40,-37,-39,-36,-34,-32,-30,-29,-28,-27,-25,-24,-23,-22,-21,-18,-46,-16,-15,-14,-13,-10,-9,-8,-6,-5,-3,-2,-35,-1,0,3,1,5,-31,7,8,9,-17,11,6,14,15,16,17,19,-19,21,20,22,23,24,-33,25,-11,26,27,28,29,30,2,31,-20,32,-4,33,34,35,36,37,-43,38,13,39,12,40,-7,41,-38,42,4,43,-44,44,-12,45,-26,46,18,47,10,48,-42,49
# Processing time (iterative_1): 4.38859s for 10,000 runs

# Iterative bubble sort 2:
# -50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
# Processing time (iterative_2): 5.08072s for 10,000 runs

# Recursive bubble sort:
# -50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
# Processing time (recursive): 8.19006s for 10,000 runs