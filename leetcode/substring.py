class Solution:
    def substring(self, s1:str,s2:str):
        len1=len(s1)
        len2=len(s2)
        for i in range(0,len1-len2):
            if s1[i:i+len2]==s2:
                return True      
        return False

if __name__=="__main__":
     s1="laboratory"
     s2="rat"
     s3="cat"
     s4="meow"
     a=Solution()
     out=a.substring(s1,s2)
     out2=a.substring(s3,s4)
     print(out)
     print(out2)
     




