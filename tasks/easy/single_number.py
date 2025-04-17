# Task: Single Number (LeetCode #136)
#
# Given: a list of integers `nums` where every element appears exactly twice, except for one
# Return the single number that appears only once
#
# This is my second solution to this task

def single_number(nums: list[int]) -> int:
    single = 0
    for n in nums:
        single ^= n
    return single


# Example calls:
print(single_number([2, 2, 1]))        # Expected output: 1
print(single_number([4, 1, 2, 1, 2]))  # Expected output: 4