class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        max_length = 0
        count = dict()
        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            
            if (right - left + 1) - max_freq <= k:
                max_length = max(max_length, (right - left + 1))
            else:
                count[s[left]] -= 1
                left += 1
        return max_length