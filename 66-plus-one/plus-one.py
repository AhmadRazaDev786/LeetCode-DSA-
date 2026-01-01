class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digit = []
        for d in digits:
            new_digit.append(str(d))
        number_str = "".join(new_digit)
        number_str = int(number_str)
        number_str +=1
        digits = []
        for d in str(number_str):
            digits.append(int(d))

        return digits