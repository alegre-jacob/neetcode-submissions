class Solution:

    def encode(self, strs: List[str]) -> str:
        c = len(strs)
        r = chr(ord('a') + c)   
        for s in strs:
            r = r + chr(ord('a') + len(s))   
        for s in strs:
            r = r + s
        return r

    def decode(self, s: str) -> List[str]:
        l = int(ord(s[0]) - ord('a')) 
        lens = [ord(s[i + 1]) - ord('a') for i in range(l)]
        tot = 1 + len(lens)
        r = []
        st = ''
        for length in lens:
            for i in range(length):
                st += s[tot + i]
            tot = tot + length
            r.append(st)
            st = ''
        return r