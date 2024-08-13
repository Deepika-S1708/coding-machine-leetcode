
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for i in s:
            if stack and stack[-1][0]==i:
                stack[-1][1]=stack[-1][1]+1
            else:
                stack.append([i,1])

            if stack[-1][1]==k:
                stack.pop()
        st="" 
        for i in stack:
            st=st+i[0]*i[1]
        print(st)
        return st
    
sp= Solution()  
s="aaaabbbee"
k=3
res=sp.removeDuplicates(s,k) 
      
    