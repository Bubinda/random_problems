from random import randrange

def quick_sort_iterative(nums: list) -> list:
    if len(nums) < 2:
        return nums
    
    index_pivot = randrange(len(nums))
    pivot = nums[index_pivot]

    greater, lesser = [],[]

    for i in nums[:index_pivot]:
        (greater if i > pivot else lesser).append(i)
    for i in nums[index_pivot+1:]:
        (greater if i > pivot else lesser).append(i)

    return quick_sort_iterative(lesser) + [pivot] + quick_sort_iterative(greater)

print(quick_sort_iterative([3,5,1,7,2,4,9,5,10,3000,4,2]))


def quick_sort_recursive(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    else:
        return [
            *quick_sort_recursive([e for e in nums[1:] if e <= nums[0]]),
            nums[0],
            *quick_sort_recursive([e for e in nums[1:] if e > nums[0]])
        ]
    
print(quick_sort_recursive([3,5,1,7,2,4,9,5,10,3000,4,2]))



if __name__ == "__main__":
    import doctest
    from random import sample
    from timeit import timeit

    doctest.testmod()

    # Benchmark: Iterative seems slightly faster than recursive.
    num_runs = 10_000
    unsorted = sample(range(-50, 50), 100)
    timer_iterative = timeit(
        "quick_sort_iterative(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nIterative quick sort:")
    print(*quick_sort_iterative(unsorted), sep=",")
    print(f"Processing time (quick_sort_iterative): {timer_iterative:.5f}s for {num_runs:,} runs")

    unsorted = sample(range(-50, 50), 100)
    timer_recursive = timeit(
        "quick_sort_recursive(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\Recursive quick sort:")
    print(*quick_sort_recursive(unsorted), sep=",")
    print(f"Processing time (quick_sort_recursive): {timer_recursive:.5f}s for {num_runs:,} runs")


# Iterative quick sort:
# -50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
# Processing time (quick_sort_iterative): 1.07761s for 10,000 runs
# \Recursive quick sort:
# -50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
# Processing time (quick_sort_recursive): 1.01953s for 10,000 runs