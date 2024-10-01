class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        positives = {}
        negatives = {}
        zeros = 0

        for x in arr:
            modulus = x % k
            if modulus == 0:    zeros+=1
            elif x > 0: positives[modulus] = positives.get(modulus,0)+1
            else:   negatives[modulus] = negatives.get(modulus,0) + 1

        print(positives, negatives)
        for i in range(1, k//2 + 1):
            if i in positives and k-i in positives:
                if i == k-i:
                    positives[i]%=2
                else:
                    subtract = min(positives[i], positives[k-i])
                    positives[i]-=subtract
                    positives[k-i]-=subtract
                if not positives[i]: del positives[i]
                if k-i in positives and not positives[k-i]: del positives[k-i]

            if i in negatives and k-i in negatives:
                if i == k-i:
                    negatives[i]%=2    
                else:
                    subtract = min(negatives[i], negatives[k-i])
                    negatives[i]-=subtract
                    negatives[k-i]-=subtract
                if not negatives[i]: del negatives[i]
                if k-i in negatives and not negatives[k-i]: del negatives[k-i]

            if i in positives and k - i in negatives:
                subtract = min(positives[i], negatives[k-i])
                positives[i]-=subtract
                negatives[k-i]-=subtract
                if not positives[i]: del positives[i]
                if not negatives[k-i]: del negatives[k-i]

            if k-i in positives and i in negatives:
                subtract = min(negatives[i], positives[k-i])
                negatives[i]-=subtract
                positives[k-i]-=subtract
                if not negatives[i]: del negatives[i]
                if not positives[k-i]: del positives[k-i]
            
        print(positives, negatives)

        return False if positives or negatives else zeros % 2 == 0 
        