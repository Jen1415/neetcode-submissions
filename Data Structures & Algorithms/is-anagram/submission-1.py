class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        print(s_dict)
        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
        
        return not any(s_dict.values())