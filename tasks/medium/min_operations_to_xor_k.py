# Task: Minimum Number of Operations to Make Array XOR Equal to K (LeetCode #2997)

# Given: a list of integers `nums` and a positive integer `k`
# You can flip any single bit in any number (binary representation) as many times as needed.
# Return the minimum number of operations required to make the XOR of all elements equal to `k


def min_operations(nums: list[int], k: int) -> int:
    xor = 0
    for n in nums:
        xor ^= n
    return bin(xor ^ k).count("1")


# 🔹 Example calls:
print(min_operations([2, 1, 3, 4], 1))  # Expected output: 2
print(min_operations([2, 0, 2, 0], 0))  # Expected output: 0

# Note: I found this improvement later.
# Starting from Python 3.10, you can use int.bit_count():
# return (xor ^ k).bit_count()