class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        output = []
        for i in range(k):
            m = max(seen, key = seen.get)
            output.append(m)
            seen[m] = 0
        return output