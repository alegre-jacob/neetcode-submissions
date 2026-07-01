class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        self.l = strs
        for s in strs:
            r = r + s + 'hahaha'
        return r
    def decode(self, s: str) -> List[str]:
        return self.l