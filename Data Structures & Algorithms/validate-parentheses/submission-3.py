class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                ans.append(s[i])
            elif len(ans)>0 and s[i]==")" and ans[-1]=="(":
                ans.pop()
            elif len(ans)>0 and s[i]=="}" and ans[-1]=="{":
                ans.pop()
            elif len(ans)>0 and s[i]=="]" and ans[-1]=="[":
                ans.pop()
            else:
                return False
        if len(ans)==0:
            return True
        else:
            return False

        