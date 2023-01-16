class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        for a in zip(*strs):
            if len(set(a)) == 1:
                res += a[0]
            else:
                return res
        return res


strs = ["flower", "flow", "flight"]

print(Solution().longestCommonPrefix(strs))
