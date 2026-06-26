class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s)).lower()
        for i in range(len(cleaned) // 2):
            if cleaned[i] == cleaned[-i-1]:
                continue
            else:
                return False
        return True