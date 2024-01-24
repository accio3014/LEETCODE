class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ""
        for i in digits:
            str_digits += str(i)

        new_num = str(int(str_digits) + 1)
        new_digits = []
        for i in range(len(new_num)):
            new_digits.append(int(new_num[i]))

        return new_digits