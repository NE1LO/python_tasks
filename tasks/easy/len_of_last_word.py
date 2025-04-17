# Task: Length of Last Word (LeetCode #58)
# 
# Given a string s containing words and spaces, return the length of the last word in the string.
# 
# Input: s = "Hello World"
# Output: 5


def length_of_last_word(s: str) -> int:
    last_word = s.split()
    return len(last_word[-1])


# Example calls:
print(length_of_last_word("Hello World"))               # Expected output: 5
print(length_of_last_word("   fly me   to   the moon "))  # Expected output: 4
print(length_of_last_word("luffy is still joyboy"))     # Expected output: 6