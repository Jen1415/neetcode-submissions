class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = {}
        for i in range(len(strs)):
            word = strs[i]
            key = "".join(sorted(word))
            hashMap.setdefault(key, []).append(word)

        return list(hashMap.values())

