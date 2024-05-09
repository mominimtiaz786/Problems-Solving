class Solution:
    myDict = {}
    
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if not len(self.myDict):
            for h in range(12):
                for m in range(60):
                    count = bin(h).count('1') + bin(m).count('1')
                    self.myDict[count] = self.myDict.get(count,[]) + [(h,m)]
        
        return [f'{h}:{m:02d}' for h,m in self.myDict.get(turnedOn,[])] 
