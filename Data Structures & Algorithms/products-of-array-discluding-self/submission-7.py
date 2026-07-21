class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        curr = 1
        for i in range(len(nums)):
            if i + 1 >= len(nums):
                break
            res[i + 1] = nums[i] * curr
            curr = res[i + 1]
        curr = 1
        for i in range(len(nums)):
            res[-i - 1] *= curr
            curr = curr * nums[-i - 1]
        return res
