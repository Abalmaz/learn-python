class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_brackets = ['(', ')', '{', '}', '[', ']']
        
        open_br = []
        
        if s == "":
            return True

        if len(s) == 1 or s[0] in dict_brackets[1::2]:
             return False

        for n in range(len(s)):
            if s[n] in dict_brackets[::2]:
                open_br.append(s[n])
            elif s[n] in dict_brackets[1::2]:
                if open_br and s[n] == dict_brackets[dict_brackets.index(open_br[-1])+1]:            		
                    open_br.pop()
                else:
                    return False 

        if open_br:
        	return False

        return True
