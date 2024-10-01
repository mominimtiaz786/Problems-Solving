class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        positives = {i:0 for i in range(k)}
        negatives = {i:0 for i in range(k)}
        zeros = 0

        for x in arr:
            modulus = x % k
            if modulus == 0:    zeros+=1
            elif x > 0: positives[modulus] = positives.get(modulus,0)+1
            else:   negatives[modulus] = negatives.get(modulus,0) + 1

        for i in range(1, k//2 + 1):
            if i == k-i:    
                positives[i]%=2
                negatives[i]%=2
            else:
                subtract = min(positives[i], positives[k-i])
                positives[i]-=subtract
                positives[k-i]-=subtract

                subtract = min(negatives[i], negatives[k-i])
                negatives[i]-=subtract
                negatives[k-i]-=subtract


            subtract = min(positives[i], negatives[k-i])
            positives[i]-=subtract
            negatives[k-i]-=subtract

            subtract = min(negatives[i], positives[k-i])
            negatives[i]-=subtract
            positives[k-i]-=subtract


        positives = {key:val for key, val in positives.items() if val}    
        negatives = {key:val for key, val in negatives.items() if val}    

        return False if positives or negatives else zeros % 2 == 0 
        