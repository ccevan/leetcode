class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        我们先从第一个字符开始，只要碰到已经出现过的字符我们就必须从之前
        出现该字符的index开始重新往后看。
        例如‘xyzxlkjh’，当看到第二个‘x’时我们就应该从y开始重新往后看了。
        那么怎么判断字符已经出现过了呢？我们使用一个hashmap，
        将每一个已经阅读过的字符作为键，而它的值就是它在原字符串中的index，
        如果我们现在的字符不在hashmap里面我们就把它加进hashmap中去，
        因此，只要目前的这个字符在该hashmap中的值大于等于了这一轮字符串的首字符，
        就说明它已经出现过了，我们就将首字符的index加1，即从后一位又重新开始读，
        然后比较目前的子串长度与之前的最大长度，取大者。
        
        res 代表目前最大子串的长度
        index 是这一轮未重复子串首字母的 index
        maps 放置每一个字符的 index，如果 maps.get(s[i], -1) 大于等于 start 的话，
        就说明字符重复了，此时就要重置 res 和 start 的值了，
        :param s:
        :return: 
        """
        index, res, n = 0, 0, len(s)
        map = {}
        for i in range(n):
            index = max(index, map.get(s[i], -1) + 1)
            res = max(res, i - index + 1)
            map[s[i]] = i
        return res
