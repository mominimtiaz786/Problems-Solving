class Solution:
    roman_encoding =  {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        resulting_integar = 0
        i = 0
        
        while i < len(s):
            if i + 1 < len(s) and self.roman_encoding[s[i]] < self.roman_encoding[s[i+1]]:
                resulting_integar+= (self.roman_encoding[s[i+1]] - self.roman_encoding[s[i]])
                i+=2
            else:
                resulting_integar+=self.roman_encoding[s[i]]
                i+=1

        return resulting_integar