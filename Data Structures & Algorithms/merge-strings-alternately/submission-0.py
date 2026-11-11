class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        c=0
        c1=0
        c2=0
        while (c1<len(word1) and c2<len(word2)):
            if c%2==0:
                ans.append(word1[c1])
                c1+=1
            else:
                ans.append(word2[c2])
                c2+=1
            c+=1
        while (c1<len(word1)):
            ans.append(word1[c1])
            c1+=1
        while (c2<len(word2)):
            ans.append(word2[c2])
            c2+=1
        return "".join(ans)

