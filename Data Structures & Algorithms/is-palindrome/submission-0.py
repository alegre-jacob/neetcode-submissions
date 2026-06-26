class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s)).lower()
        for i in range(len(cleaned) // 2):
            if cleaned[0] == cleaned[-1]:
                cleaned = cleaned[1:-1]
            else:
                return False
        return True