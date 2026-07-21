class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 0
        numZero = 0
        for num in nums:
            if num != 0 and total == 0 and numZero == 0:
                total = 1
            if num == 0:
                numZero += 1
            else:
                total = total * num
        res = []
        for num in nums:
            if numZero == 0:
                res.append(total // num)
            else:
                if numZero > 1:
                    res.append(0)
                elif num == 0:
                    res.append(total)
                else:
                    res.append(0)
        return res