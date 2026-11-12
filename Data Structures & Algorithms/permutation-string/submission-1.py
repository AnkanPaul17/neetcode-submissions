class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq={}
        for i in range(len(s1)):
            if s1[i] not in freq:
                freq[s1[i]]=1
            else:
                freq[s1[i]]+=1
        temp={}
        l=0
        for i in range(len(s2)):
            if s2[i] in freq:
                if s2[i] not in temp:
                    temp[s2[i]]=1
                else:
                    temp[s2[i]]+=1
                while temp[s2[i]]>freq[s2[i]]:
                    temp[s2[l]]-=1
                    if temp[s2[l]]==0:
                        del temp[s2[l]]
                    l+=1
                if temp==freq:
                    return True
            else:
                temp.clear()
                l=i+1
        return False

        