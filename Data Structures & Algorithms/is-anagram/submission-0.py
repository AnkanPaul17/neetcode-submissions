class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS={}
        freqT={}
        for i in s:
            if i not in freqS:
                freqS[i]=1
            else:
                freqS[i]+=1
        for i in t:
            if i not in freqT:
                freqT[i]=1
            else:
                freqT[i]+=1
        if freqS==freqT:
            return True
        else:
            return False

        