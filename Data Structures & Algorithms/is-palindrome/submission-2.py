class Solution:
    @classmethod
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        newS = ""
        for char in s:
            if char.isalnum():
                newString = char + newString
                newS += char
        return newS.lower() == newString.lower()