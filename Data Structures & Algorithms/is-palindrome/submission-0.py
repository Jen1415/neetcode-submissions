import re
class Solution:
    @classmethod
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        result = re.sub(r"[^\w\s]", "", s)
        return result == result[::-1]
        