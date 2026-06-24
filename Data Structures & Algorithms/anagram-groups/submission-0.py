class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            srt = "".join(sorted(s))
            if srt in seen:
                seen[srt] = seen[srt] + [s]
            else:
                seen[srt] = [s]
        total = []
        for i in seen:
            total.append(seen[i])
        return total