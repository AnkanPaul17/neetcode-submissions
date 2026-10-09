class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        ans=[]
        n=min(len(first), len(last))
        for i in range(n):
            if first[i]==last[i]:
                ans.append(first[i])
            else:
                return "".join(ans)
        return "".join(ans)