def shift_zeros_1(nums: list) -> list:
    """
    >>> shift_zeros([0, 1, 0, 3, 12])
    [1, 3, 12, 0, 0]
    """
    for idx, value in enumerate(nums):
        if value == 0:
            nums.append(value)
            nums.pop(idx)
    return nums


def shift_zeros_2(nums: list) -> list:
    """
    >>> shift_zeros([0, 1, 0, 3, 12])
    [1, 3, 12, 0, 0]
    """
    temp = []
    zero_count = 0
    for i in nums:
        if i == 0:
            zero_count += 1
        else:
            temp.append(i)
    return temp + [0]*zero_count


import random
import time
n = 200000
array = [random.randint(0,9) for _ in range(n)]
start= time.time()
shift_zeros_1(array)
end = time.time()
print(end-start)
start2= time.time()
shift_zeros_2(array)
end2 = time.time()
print(end2-start2)
