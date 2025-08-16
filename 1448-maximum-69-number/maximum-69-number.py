class Solution:
    def maximum69Number (self, num: int) -> int:
        numi = list(map(int, str(num)))

        for i in range(len(numi)):
            if numi[i] == 6:
                numi[i] = 9
                break
        num = int("".join(map(str, numi)))
        return num