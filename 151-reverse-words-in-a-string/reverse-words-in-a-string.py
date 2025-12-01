class Solution:
    def reverseWords(self, s: str) -> str:
        N = len(s)
        reversed_string = ""

        i=0
        j=0

        while j<N and i<N:
            while i<N and s[i]==" ": i+=1
            if i == N:  break

            j=i
            while j<N and s[j]!=" ":
                j+=1
            
            word = s[i:j]
            reversed_string = (word+" "+reversed_string) if reversed_string else (word)

            i=j
        
        return reversed_string


        