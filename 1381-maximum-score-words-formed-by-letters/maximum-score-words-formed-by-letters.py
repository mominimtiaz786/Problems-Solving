class Solution:
    # def checkIsValid(self, words, lettersCount):
    #     wordsLetterCounter = dict()
    #     for word in words:
    #         for ch in word:
    #             wordsLetterCounter[ch] = wordsLetterCounter.get(ch,0) + 1

    #     for letter in wordsLetterCounter:
    #         if wordsLetterCounter[letter] > lettersCount.get(letter, 0):
    #             return False

    #     return True
    

    # def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
    #     lettersCount = Counter(letters)
    #     letters = set(letters)
    #     N = len(words)

    #     lettersScoreDict = {
    #         chr(i + ord('a')): score[i] if chr(i + ord('a')) in letters else -float('inf')
    #         for i in range(26)
    #     }

    #     wordScores = [
    #         sum([lettersScoreDict[ch] for ch in word]) 
    #         for word in words
    #         ]


    #     maxSum = 0
    #     for i in range(2**N):
    #         wordsComb = []
    #         combSum = 0
    #         x = i
    #         while x:
    #             msb = math.floor(math.log2(x))
    #             wordsComb.append(words[msb])
    #             combSum+=wordScores[msb]
    #             x^=(1<<msb)
            
    #         if combSum > 0 and self.checkIsValid(wordsComb, lettersCount):
    #             maxSum = max(maxSum, combSum)
        
    #     return maxSum

    def combSum(self, words, lettersCount, score):
        combSum = 0 
        wordsLetterCounter = dict()
        for word in words:
            for ch in word:
                wordsLetterCounter[ch] = wordsLetterCounter.get(ch,0) + 1

        for letter in wordsLetterCounter:
            if wordsLetterCounter[letter] > lettersCount.get(letter, 0):
                return 0
            else:
                combSum+=(wordsLetterCounter[letter]*score[(ord(letter)- ord('a'))])

        return combSum
    

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lettersCount = Counter(letters)
        # letters = set(letters)
        N = len(words)

        # lettersScoreDict = {
        #     chr(i + ord('a')): score[i] if chr(i + ord('a')) in letters else -float('inf')
        #     for i in range(26)
        # }

        # wordScores = [
        #     sum([lettersScoreDict[ch] for ch in word]) 
        #     for word in words
        #     ]


        maxSum = 0
        for i in range(2**N):
            wordsComb = []
            x = i
            while x:
                msb = math.floor(math.log2(x))
                wordsComb.append(words[msb])
                x^=(1<<msb)
            
            maxSum = max(maxSum, self.combSum(wordsComb, lettersCount, score))
        
        return maxSum