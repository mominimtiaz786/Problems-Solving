class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j, leng = 0, len(needle), len(haystack)
        occurance = -1

        while j <= leng:
            if haystack[i:j] == needle:
                return i
            else:
                i+=1
                j+=1
        return occurance