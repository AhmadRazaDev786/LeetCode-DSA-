class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # Continue until `num` is a single-digit number
            num = sum(int(digit) for digit in str(num))  # Convert number to digits and sum them
        return num