class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curr = 0
        mini = 0
        while l < len(nums) - 1:
            if l == r:
                curr = nums[r]
            if curr < target and r != len(nums) - 1:
                r += 1
                curr = curr + nums[r]
            elif curr >= target:
                if mini == 0:
                    mini = len(nums)
                mini = min(r - l + 1, mini)
                curr = curr - nums[l]
                l += 1
            else: 
                curr = curr - nums[l]
                l += 1

        if len(nums) == 1:
            if nums[0] >= target:
                return 1
        if curr >= target:
            mini = min(r-l + 1, mini)
        return mini
            