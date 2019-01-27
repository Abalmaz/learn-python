class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 1
        if x < 0:
            n = -1
        out_num = int(str(x*n)[::-1])*n
        return out_num if -2**31 < out_num < 2**31 else 0
