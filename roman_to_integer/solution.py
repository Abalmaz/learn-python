roman = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
arab = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

def convert(n):
    if n in roman:
        return arab[roman.index(n)]
    elif n in arab:
        return roman[arab.index(n)]
    else:
        return "Sorry, you entered not roman or arabic number"

class Solution(object):
    def romanToInt(self, num):
        result, i = 0, 0
        while i < len(num):
            curr_val = 0
            if i < len(num)-1 and convert(num[i]) < convert(num[i+1]):
                curr_val = num[i] + num[i+1]
                i += 2
            else:
                curr_val = num[i]
                i += 1

            if curr_val in roman:
                result += convert(curr_val)
            else:
                return "Incorrect roman numeral"
        return result
