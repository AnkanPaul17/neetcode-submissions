class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in range(len(operations)):
            if operations[i] not in ["+", "D", "C"]:
                ans.append(operations[i])
            elif operations[i]=="+":
                temp1=int(ans[-1])
                temp2=int(ans[-2])
                ans.append(temp1+temp2)
            elif operations[i]=="D":
                temp3=int(ans[-1])
                ans.append(2*temp3)
            else:
                ans.pop()
        total=0
        for i in range(len(ans)):
            total+=int(ans[i])
        return total
        