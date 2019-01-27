class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) > 1:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                     if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                        return strs[0][:i]        
        return strs[0]
