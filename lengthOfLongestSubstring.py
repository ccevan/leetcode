class Solution:
    def lengthOfLongestSubstring(self, s):
        index, res, n = 0, 0, len(s)
        map = {}
        for i in range(n):
            index = max(index, map.get(s[i], -1) + 1)
            res = max(res, i - index + 1)
            map[s[i]] = i
        return res